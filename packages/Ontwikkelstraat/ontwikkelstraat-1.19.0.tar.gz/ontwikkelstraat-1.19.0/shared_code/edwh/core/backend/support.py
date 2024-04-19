import binascii
import datetime
import getpass
import os
import time
from typing import Callable

import edwh.core.pgcache.define_models
import tabulate
from attrs import define, field
from edwh.core.applog.diskcachesink import DequeSink
from edwh.core.applog.signalemitter import SignalEmitter
from edwh.core.applog.sink import SignalSink
from edwh.core.applog.tasks import process_applog_batch
from edwh.core.backend import engine
from edwh.core.backend.ntfy_sh import Priority, View, error, notify, onbekend, warning
from edwh.core.data_model import setup_db_tables
from edwh_migrate import setup_db
from invoke import task
from pydal import DAL


class Environment:
    db: DAL = field(init=False)
    sink: SignalSink = field(init=False)
    backend: engine.Backend = field(init=False)
    username: str = field(init=False)
    error: Callable = field(init=False, default=error)
    warning: Callable = field(init=False, default=warning)
    onbekend: Callable = field(init=False, default=onbekend)
    notify: Callable = field(init=False, default=notify)

    def __init__(self, long_running=False):
        self.db = edwh.core.pgcache.define_models.define_model(
            setup_db_tables(setup_db(long_running=long_running))
        )
        app_id = os.getenvb(b"TOOLS_APPLOG_ID")
        app_key = binascii.unhexlify(os.getenvb(b"TOOLS_APPLOG_KEY"))
        # /!\ autocommit is false, so the server MUST .commit AFTER the response is written to the socket, if possible.
        self.sink = DequeSink(
            process_applog_batch,
            app_id,
            app_key,
            autocommit=True,
        )
        self.backend = engine.Backend(
            self.db,
            sink=self.sink,
            applog=SignalEmitter(
                signal_processor=self.sink,
                signal_source="edwh.core.backend.support",
                session_gid=None,
                user_gid=None,
                timestamp=datetime.datetime.now(),
                origin_domain=os.getenv("HOSTINGDOMAIN"),
            ),
        )
        self.username = getpass.getuser()


@task()
def set_password(ctx, email, password=None):
    env = Environment()
    user = env.backend.user(email=email)
    print(user)
    if not password:
        password = getpass.getpass(f"Password for {email}:")
    with env.db.single_transaction() as db:
        row = db.user(gid=user.id)
        row.update_record(password=engine.hash_password(password))
    env.backend.applog.reset_password(user.email)


unwanted_keys = ["found_tiles_gids", "hardware"]


@task()
def monitor_applog(ctx, n=50):
    env = Environment()
    db = env.db
    last_id = None
    view_rows = []
    try:
        while True:
            id_clause = (db.signal.id > last_id) if last_id else (db.signal.id > 0)
            top = (0, n) if not last_id else (0, 1000)  # get all rows since last id
            rows = (
                db((db.evidence.id == db.signal.evidence_id) & id_clause)
                .select(
                    db.signal.id,
                    db.signal.ts,
                    db.signal.name,
                    db.signal.source,
                    db.signal.session_gid,
                    db.signal.user_gid,
                    db.evidence.source,
                    orderby=~db.signal.ts,
                    limitby=top,
                )
                .as_list()
            )[::-1]
            if not rows:
                time.sleep(0.25)
                continue
            last_id = max(row["signal"]["id"] for row in rows)
            rows = [{**row["signal"], **row["evidence"]["source"]} for row in rows]
            for row in rows:
                del row["id"]
            for row in rows:
                for unwanted in unwanted_keys:
                    if unwanted in row:
                        del row[unwanted]
            view_rows.extend(rows)
            view_rows = view_rows[len(view_rows) - n :]
            print(tabulate.tabulate(view_rows, headers="keys"))
    except KeyboardInterrupt:
        env.db.close()


@task()
def cache_size(ctx, env=None):
    env = Environment() if env is None else env
    db = env.db
    rows = db.executesql(
        """
    select pg_size_pretty(pg_relation_size('cache')) as table_only, pg_size_pretty(pg_total_relation_size('cache')) as total;
    """
    )
    print(tabulate.tabulate(rows, headers=["just the tables", "total size"]))
    db.close()


@task()
def database_connections(ctx, env=None):
    env = Environment() if env is None else env
    db = env.db
    rows = db.executesql(
        """
        SELECT backend_type, state, application_name, usename, query, backend_start, query_start, state_change
          FROM pg_stat_activity
         order by state_change desc 
        """
    )
    print(
        tabulate.tabulate(
            rows,
            headers=[
                "backend_type",
                "state",
                "application name",
                "username",
                "query",
                "backend start",
                "query start",
                "state change",
            ],
        )
    )
    db.close()


@task()
def cache_info(ctx, env=None, n=10):
    env = Environment() if env is None else env
    cache_size(ctx, env)
    db = env.db
    rows = db.executesql(
        """
    select reads, gid, ts, lr, length(value) from cache order by reads desc, length desc limit %s ;
    """,
        placeholders=(n,),
    )
    print(tabulate.tabulate(rows, headers="reads,gid,ts,lr,len".split(",")))


@task()
def update_opengraph(ctx, env=None):
    import edwh.core.backend.tasks

    edwh.core.backend.tasks.update_opengraph_all.delay()


@task()
def show_table_sizes(ctx, env=None):
    env = Environment() if env is None else env
    db = env.db
    rows = db.executesql(
        """
    SELECT
        y.nspname ||'.'|| relname AS "namespace.table",
        pg_size_pretty (
            pg_total_relation_size (X .oid)
        ) AS "size"
    FROM
        pg_class X
    LEFT JOIN pg_namespace Y ON (Y.oid = X .relnamespace)
    WHERE
        nspname NOT IN (
            'pg_catalog',
            'information_schema'
        )
    AND X .relkind <> 'i'
    AND nspname !~ '^pg_toast'
    ORDER BY
        pg_total_relation_size (X .oid) desc
    """
    )
    print(tabulate.tabulate(rows, headers="namespace.table, size".split(",")))


@task()
def shrink_database_for_development(ctx, env=None):
    env = Environment() if env is None else env
    db = env.db
    for tablename in [
        "api_activity",
        "event_stream",
        "session",
        "api_activity",
        "public.signal",
        "public.evidence",
    ]:
        print("Truncating", tablename, "...")
        rows = db.executesql(f"truncate table {tablename} cascade ;")
        db.commit()
    print("truncating done")
    show_table_sizes(ctx, env=env)
