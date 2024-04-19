import datetime
import hashlib
import json
import os
import sys
from datetime import datetime, timedelta
from uuid import UUID

from attrs import define
from celery import Celery
from diskcache import Deque
from pydal import DAL
from ycecream import y

from .. import setup_db, setup_db_tables

Row = DAL.Row

scheduler = Celery(
    "edwh.core.applog.tasks",
    broker=os.getenv("APPLOG_CELERY_BROKER")
    # TODO: omgevingsvariabele van maken, komt ook elders voor.
)

ONE_MINUTE = timedelta(seconds=60)
db = setup_db(migrate=False, migrate_enabled=False, appname=" ".join(sys.argv))
setup_db_tables(db)
deque = Deque(directory="/shared_applog")


@define
class SignalAndEvidenceRows:
    signal: Row
    evidence: Row | None


def truncate_to_minute(timestamp: datetime) -> datetime:
    return timestamp - timedelta(
        seconds=timestamp.second, microseconds=timestamp.microsecond
    )


def save_applog_evidence(db: DAL, session, source) -> Row:
    # bereken de hash_value van de json payload.
    # EDIT DEZE JSON NIET, DIE MOET GESORTEERD ZIJN OM DUPLICATEN TE VOORKOMEN
    hash_value = hashlib.sha1(json.dumps(source).encode("utf-8")).hexdigest()
    # zoek bestaand bewijs
    evidence = db(db.evidence.sha1_digest == hash_value).select(limitby=(1, 1)).first()
    if not evidence:
        # als geen bestaand bewijs, maak nieuw bewijs
        new_evidence_id = db.evidence.insert(
            session_gid=session, source=source, sha1_digest=hash_value
        )
        evidence = db.evidence[new_evidence_id]
    return evidence


def process_applog_signal(
    name: str,
    signal_source: str,
    evidence: str | UUID | None = None,
    session_gid: str | UUID | None = None,
    user_gid: str | UUID | None = None,
    ts: datetime = None,
    related: str | UUID | None = None,
):
    signal_fields = dict(
        name=name,
        source=signal_source,
        ts=ts if ts else db.signal.ts.default(),
        user_gid=user_gid,
        session_gid=session_gid,
        related=related,
    )
    if evidence is not None:
        evidence = save_applog_evidence(db, session_gid, evidence)
        # maak nieuw signaal verwijzend naar bestaand of nieuw bewijs
        signal_fields.update(
            dict(
                evidence_id=evidence.id,
                evidence_gid=evidence.gid,
            )
        )
    else:
        if session_gid is not None:
            raise ValueError(
                "Session_gid was provided, but no evidence was provided. Session data will be lost."
            )
        evidence = None
    new_signal_id = db.signal.insert(**signal_fields)
    # truncate from here when nameko service: events are fire-and-forget,
    # return values are invalid
    # new_signal = db.signal[new_signal_id]
    # return SignalAndEvidenceRows(signal=new_signal, evidence=evidence)


@scheduler.task()
def process_applog_buffer(events: list[dict]) -> None:
    """Processes all the received events from the events buffer using process_applog_signal."""
    successful_signals = 0
    failed_signals = []
    db._adapter.reconnect()
    for event in events:
        try:
            print(
                "{signal_source}/{name} ({short_related}...)".format(
                    **event, short_related=event["related"][:8]
                )
            )
            process_applog_signal(
                name=event["name"],
                signal_source=event["signal_source"],
                evidence=event.get("evidence"),
                session_gid=event.get("session_gid"),
                user_gid=event.get("user_gid"),
                ts=event.get("ts"),
                related=event.get("related"),
            )
            successful_signals += 1
        except Exception as e:
            try:
                db.rollback()
            except Exception as e:
                print("rollback failed in process_applog_buffer:", e)
                db.close()
            # waarschijnlijk invalide data
            print("[stats]", "Incorrecte Data", event, e)
            failed_signals.append(event)
    db.commit()
    db.close()
    print(f"Successful: {successful_signals}, failed: {repr(failed_signals)}")
    return


@scheduler.task()
def process_applog_batch(json_signal_batch: str) -> None:
    """Process a json string of one or more events using process_applog_buffer."""
    print(f"process_applog_batch: processing {len(json_signal_batch)} events")
    event_or_events = json.loads(json_signal_batch)
    events = [event_or_events] if isinstance(event_or_events, dict) else event_or_events
    return process_applog_buffer(events)


@scheduler.task()
def update_applog_stats() -> None:
    print(f"update_applog_stats")
    # def count_minute_statistics(self):
    last_unused_signal_count = -1
    while True:
        #### go figure the last seen
        # get last seen minute from the cumulated stats
        last_known = (
            db(db.counts_per_minute)
            .select(db.counts_per_minute.ts.max())
            .first()[db.counts_per_minute.ts.max()]
        )
        y(last_known)
        if last_known is None:
            # no cumulated statistics have been saved yet, get the first signals's timestamp
            first_signal_ts = (
                db(db.signal).select(db.signal.ts.min()).first()[db.signal.ts.min()]
            )
            if not first_signal_ts:
                print("no first_signal_ts")
                break  # for now

            last_known = truncate_to_minute(first_signal_ts)
        else:
            # crop at exact second of that minute
            last_known = truncate_to_minute(last_known) + ONE_MINUTE
        y(last_known)

        last_stats = (
            db(db.counts_per_minute)
            .select(db.counts_per_minute.ts.max())
            .first()[db.counts_per_minute.ts.max()]
        )
        if last_stats is None:
            # no data available yet? start one minute before the last known evidence.
            last_stats = last_known - ONE_MINUTE

        ten_minutes_ago = datetime.now() - timedelta(minutes=10)
        ready_to_handle_signals = db(
            (db.signal.ts < ten_minutes_ago) & (db.signal.ts > last_stats)
        ).count()
        if (y(ready_to_handle_signals) == 0) or (
            last_unused_signal_count == ready_to_handle_signals
        ):
            print("Done for now")
            break
        else:
            last_unused_signal_count = ready_to_handle_signals

        # this is last known, so we calculate for everything a minute later.
        when = last_known + ONE_MINUTE
        if y((datetime.now() - when).seconds) < 600:
            # break the loop when to close to now.
            # give processes some slack to report their stats
            print("Done with loop")
            break

        when_start = truncate_to_minute(when)
        when_stop = when_start + ONE_MINUTE
        stat_sql = {
            "api-activity": "select count(*) from signal where name='browse-items' and ts between %s and %s",
            "items-read": "select count(*) from signal where name='search' and ts between %s and %s",
        }
        evidenced_sql = {
            "new-user-count": "select gid from signal where name='new-user' and ts between %s and %s"
        }
        for name, sql in stat_sql.items():
            count = db.executesql(sql, placeholders=(when_start, when_stop))[0][0]
            # print(name,sql,count)
            if count:
                db.counts_per_minute.insert(
                    ts=when_start,
                    count=count,
                    name=name,
                )
                y(db._lastsql)
        for name, sql in evidenced_sql.items():
            source = db.executesql(sql, placeholders=(when_start, when_stop))
            count = len(source)
            source = json.dumps(source)
            # print(name,sql,source)
            evidence = save_applog_evidence(db, None, source)
            if count:
                db.counts_per_minute.insert(
                    evidence_gid=evidence.gid,
                    evidence_id=evidence.id,
                    ts=when_start,
                    count=count,
                    name=name,
                )
                y(db._lastsql)
        db.commit()
        db.close()
    return


@scheduler.task()
def process_deque() -> None:
    """Process the deque filled by the diskcachesink.DequeSink.

    Eagerly reads from the deque and feeds this to the process_applog_batch function.
    """
    buffer = []
    try:
        while len(buffer) < 50:
            event_or_events = json.loads(deque.popleft())
            events = (
                [event_or_events]
                if isinstance(event_or_events, dict)
                else event_or_events
            )
            buffer.extend(events)
    except IndexError:
        # deque is empty.
        pass
    if buffer:
        return process_applog_buffer(buffer)


# -----------------------------------------------------
scheduler.conf.beat_schedule = {
    "update_applog_stats": {
        "task": "edwh.core.applog.tasks.update_applog_stats",
        "schedule": 15 * 60,
        "args": (),
    },
    "process_deque": {
        "task": "edwh.core.applog.tasks.process_deque",
        "schedule": 3,
        "args": (),
    },
}
