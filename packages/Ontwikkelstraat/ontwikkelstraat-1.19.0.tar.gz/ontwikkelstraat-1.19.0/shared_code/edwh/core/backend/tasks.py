"""
To use celery tasks:
1) pip install -U "celery[redis]"
2) In settings.py:
   USE_CELERY = True
   CELERY_BROKER = "redis://localhost:6379/0"
3) Start "redis-server"
4) Start "celery -A apps.{appname}.tasks beat"
5) Start "celery -A apps.{appname}.tasks worker --loglevel=info" for each worker

Retries, see http://www.ines-panker.com/2020/10/29/retry-celery-tasks.html

"""
import base64
import binascii
import json
import os
import tempfile
import textwrap
import time
from datetime import datetime
from pathlib import Path
from uuid import UUID, uuid4

import httpx
from celery import Celery
from edwh.core.backend import opengraph
from edwh.core.backend.support import Environment
from edwh.core.backend.ntfy_sh import Priority, View, error, notify, onbekend, warning
from edwh.core.data_model import setup_db_tables, Visibility
from edwh_migrate import setup_db
from plumbum import local
from pydal import DAL


# todo: retries gebruiken, en kijken of signals te gebruiken zijn om timeouts enzo op te vangen.


def required_env(key):
    """
    Checks if the specified environment variable is set and returns its value.

    This function takes a key as input and retrieves the corresponding value from the environment variables using
    `os.getenv()`. If the value is not found, it raises an `EnvironmentError` with a message indicating that the
    required key is not found. Otherwise, it returns the value.

    Args:
        key: The name of the environment variable to check.

    Returns:
        The value of the specified environment variable.

    Raises:
        EnvironmentError: If the required key is not found in the environment variables.

    Examples:
        value = required_env("API_KEY")
    """

    value = os.getenv(key)
    if value is None:
        raise EnvironmentError(f"Required key {key} not found.")
    return value


Row = DAL.Row
scheduler = Celery(
    "edwh.core.backend.tasks", broker=required_env("BACKEND_CELERY_BROKER")
)


class MailgunError(RuntimeError):
    pass


@scheduler.task(bind=True, max_retries=int(required_env("MAILGUN_MAX_RETRIES")))
def outbound_email_verification_code(
    self, receiver_name: str, code: str, to_email: str, from_email: str = None
):
    try:
        to_email = to_email.replace("@roc.nl", "@edwh.nl")
        from_email = from_email or required_env("DEFAULT_FROM_ADDRESS")
        mailgun_url = (
            f"https://api.eu.mailgun.net/v3/{required_env('MAILGUN_DOMAIN')}/messages"
        )
        result = httpx.post(
            mailgun_url,
            auth=("api", required_env("MAILGUN_API_KEY")),
            data={
                "from": from_email,
                "to": [to_email],
                "text": textwrap.dedent(
                    f"""
                Beste {receiver_name}, 
    
                Gebruikt code "{code}" om je email adres te valideren. 
                Bij de volgende keer dat je inlogt met dit email adres wordt je om deze code gevraagd. 
    
                Mocht je geen account hebben aangemaakt op het delen.meteddie.nl netwerk, kun je dit bericht negeren. 
                Je mag ons ook melden dat er mogelijk misbruik gemaakt wordt van je naam, neem daarvoor contact met ons op
                door te reageren op deze email. 
    
                Met vriendelijke groet, 
                Eddie. 
                """
                ),
                "subject": "Verificatie van je email adres voor het MetEddie netwerk. ",
            },
        )
        print("MAILGUN REQUEST:", result.request.content)
        print("MAILGUN RESPONSE:", result.text)
        if result.json().get("message") != "Queued. Thank you.":
            message = (
                f"Mailgun error (sending email verifcation code to {to_email}): "
                + result.text
            )
            error(message)
            raise MailgunError(message)
    except:
        self.retry(
            countdown=eval(
                required_env("MAILGUN_NEXT_RETRY_DELAY_EXPRESSION"),
                dict(),
                dict(retries=self.request.retries),
            )
        )
        raise
    return result


@scheduler.task(bind=True, max_retries=int(required_env("MAILGUN_MAX_RETRIES")))
def outbound_email_new_password(
    self, receiver_name: str, password: str, to_email: str, from_email: str = None
):
    try:
        to_email = to_email.replace("@roc.nl", "@edwh.nl")
        from_email = from_email or required_env("DEFAULT_FROM_ADDRESS")
        mailgun_url = (
            f"https://api.eu.mailgun.net/v3/{required_env('MAILGUN_DOMAIN')}/messages"
        )
        print(mailgun_url)
        print(required_env("MAILGUN_API_KEY"))
        result = httpx.post(
            mailgun_url,
            auth=("api", required_env("MAILGUN_API_KEY")),
            data={
                "from": from_email,
                "to": [to_email],
                "text": textwrap.dedent(
                    f"""
                Beste {receiver_name}, 
    
                Op verzoek sturen we je een nieuw wachtwoord toe. 
                Log in op https://delen.meteddie.nl of een ander platform van EducationWarehouse met het volgende wachtwoord: {password}
    
                We raden je aan om na het inloggen je wachtwoord te wijzigen in een beter te onthouden wachtwoord. 
                Als je ingelogd bent, klik dan op het poppetje-icoon rechtsboven; klik dan op "mijn profiel" en dan "profiel aanpassen".
                Je kunt nu je wachtwoord wijzigen en opslaan. 
    
                Met vriendelijke groet, 
                Eddie. 
                """
                ),
                "subject": "Nieuw wachtwoord op het MetEddie netwerk. ",
            },
        )
        print("MAILGUN REQUEST:", result.request.content)
        print("MAILGUN RESPONSE:", result.text)

        if result.json().get("message") != "Queued. Thank you.":
            if result.json().get("message") != "Queued. Thank you.":
                message = (
                    f"Mailgun error (sending new password email to {receiver_name}): "
                    + result.text
                )
                error(message)
                raise MailgunError(message)
    except:
        self.retry(
            countdown=eval(
                required_env("MAILGUN_NEXT_RETRY_DELAY_EXPRESSION"),
                dict(),
                dict(retries=self.request.retries),
            )
        )
        raise

    return result


@scheduler.task(bind=True, max_retries=int(required_env("MAILGUN_MAX_RETRIES")))
def outbound_email_ask_question(
    self,
    receiver_name: str,
    to_email: str,
    webuser_name: str,
    webuser_email: str,
    item_title: str,
    item_permalink: str,
    question: str,
    from_email: str = None,
):
    try:
        to_email = to_email.replace("@roc.nl", "@edwh.nl")
        from_email = from_email or required_env("DEFAULT_FROM_ADDRESS")
        mailgun_url = (
            f"https://api.eu.mailgun.net/v3/{required_env('MAILGUN_DOMAIN')}/messages"
        )
        print(mailgun_url)
        result = httpx.post(
            mailgun_url,
            auth=("api", required_env("MAILGUN_API_KEY")),
            data={
                "from": from_email,
                "to": [to_email],
                "text": textwrap.dedent(
                    f"""
                Beste {receiver_name}, 
    
                Onderwijs-collega {webuser_name} reageerde op jouw artikel "{item_title}" met:
    
                {textwrap.indent(question, '> ')}
    
                Beantwoord {webuser_name} door te mailen naar {webuser_email}.    
                Wil je je eigen artikel eerst teruglezen? Kijk op {item_permalink}. 
    
    
                Met vriendelijke groet, 
                Eddie. 
                """
                ),
                "subject": f"Reactie {item_title}. ",
            },
        )
        print("MAILGUN REQUEST:", result.request.content)
        print("MAILGUN RESPONSE:", result.text)

        if result.json().get("message") != "Queued. Thank you.":
            message = (
                f"Mailgun error (sending question from {webuser_email} to {to_email} about {item_permalink}: {question}): "
                + result.text
            )
            error(message)
            raise MailgunError(message)
    except:
        self.retry(
            countdown=eval(
                required_env("MAILGUN_NEXT_RETRY_DELAY_EXPRESSION"),
                dict(),
                dict(retries=self.request.retries),
            )
        )
        raise
    return result


@scheduler.task(bind=True, max_retries=int(required_env("MAILGUN_MAX_RETRIES")))
def outbound_email_validate_for_claim(
    self,
    to_email: str,
    item_title: str,
    message: str,
    validation_link: str,
    from_email: str = None,
):
    try:
        to_email = to_email.replace("@roc.nl", "@edwh.nl")
        from_email = from_email or required_env("DEFAULT_FROM_ADDRESS")
        mailgun_url = (
            f"https://api.eu.mailgun.net/v3/{required_env('MAILGUN_DOMAIN')}/messages"
        )
        print(mailgun_url)
        result = httpx.post(
            mailgun_url,
            auth=("api", required_env("MAILGUN_API_KEY")),
            data={
                "from": from_email,
                "to": [to_email],
                "text": textwrap.dedent(
                    f"""
                Beste onderwijs professional, 
                
                Je hebt aangegeven eigenaarschap te claimen voor artikel "{item_title}". Hartelijk dank daarvoor!
                Door jouw claim kunnen onderwijs collega's jou bereiken. 
                
                Je gaf hierbij aan: 
                
                {textwrap.indent(message, '> ')}
                
                Aangezien veel robots op internet onze formulieren invullen en op onze knoppen klikken willen we graag zeker 
                weten dat jij dit bericht gelezen hebt. Klik daarom op onderstaande link om je eigenaarschap te bevestigen. 
                Mocht klikken niet werken, kun je de link ook kopiëren en plakken in je browser.
                
                {validation_link}.
                
                Heb je je bedacht en wil je geen eigenaarschap claimen of heb je überhaupt niet verzocht, negeer dan deze email.
                
                Met vriendelijke groet, 
                Eddie. 
                """
                ),
                "subject": f"Claim op {item_title}. ",
            },
        )
        print("MAILGUN REQUEST:", result.request.content)
        print("MAILGUN RESPONSE:", result.text)

        if result.json().get("message") != "Queued. Thank you.":
            message = f"Mailgun error (sending claim to {to_email} about '{item_title}': {message}): {result.text}"
            error(message)
            raise MailgunError(message)
    except:
        self.retry(
            countdown=eval(
                required_env("MAILGUN_NEXT_RETRY_DELAY_EXPRESSION"),
                dict(),
                dict(retries=self.request.retries),
            )
        )
        raise
    return result


@scheduler.task(bind=True, max_retries=int(required_env("MAILGUN_MAX_RETRIES")))
def outbound_email_claim_notification_to_eddie(
    self,
    item_title: str,
    item_permalink: str,
    is_authenticated: bool,
    user_name: str | None,
    user_email: str,
    user_phone: str,
    message: str,
):
    try:
        to_email = required_env("EDDIE_EMAIL")
        from_email = required_env("DEFAULT_FROM_ADDRESS")
        mailgun_url = (
            f"https://api.eu.mailgun.net/v3/{required_env('MAILGUN_DOMAIN')}/messages"
        )
        print(mailgun_url)
        result = httpx.post(
            mailgun_url,
            auth=("api", required_env("MAILGUN_API_KEY")),
            data={
                "from": from_email,
                "to": [to_email],
                "text": textwrap.dedent(
                    f"""
                Eddie, 
                
                {user_name if is_authenticated else 'Iemand'} heeft aangegeven eigenaarschap te claimen op artikel "{item_title}".  
                Het artikel vind je op {item_permalink}.
                
                Gebruiker maakte de opmerking:
                
                {textwrap.indent(message, '> ')}
                
                tel: {user_phone}
                email: {user_email}
                heeft al een account: {'Ja' if is_authenticated else 'Nee'}
                
                
                Met vriendelijke groet, 
                Eddie. 
                """
                ),
                "subject": f"Claim op {item_title}. ",
            },
        )
        print("MAILGUN REQUEST:", result.request.content)
        print("MAILGUN RESPONSE:", result.text)

        if result.json().get("message") != "Queued. Thank you.":
            message = f"Mailgun error (sending claim to {to_email} about '{item_title}': {message}): {result.text}"
            error(message)
            raise MailgunError(message)
    except:
        self.retry(
            countdown=eval(
                required_env("MAILGUN_NEXT_RETRY_DELAY_EXPRESSION"),
                dict(),
                dict(retries=self.request.retries),
            )
        )
        raise
    return result


@scheduler.task
def update_materialized_view_mv__item_tags():
    """
    This code updates the materialized view mv__item_tags in the database.
    It executes the SQL statement REFRESH MATERIALIZED VIEW mv__item_tags; to update the view.
    After the update is complete, it commits the changes to the database.
    """
    db = setup_db(appname="Materialze mv__item_tags")
    try:
        start_time = time.time()
        db.executesql(
            """
        REFRESH MATERIALIZED VIEW mv__item_tags;
        """
        )
        duration = time.time() - start_time
        print(f"materialiation of mv__item_tags complete in {duration} seconds")
        db.commit()
    finally:
        db.close()


@scheduler.task
def update_materialized_view_mv__tag_arrays():
    """
    Updates the materialized view `mv__tag_arrays`.

    This function refreshes the materialized view `mv__tag_arrays` in the database.
    It executes the SQL statement `REFRESH MATERIALIZED VIEW mv__tag_arrays;` to update the view.
    After the update is complete, it commits the changes to the database.

    Args:
        self: The instance of the function.

    Returns:
        None.

    Raises:
        None.

    Examples:
        update_materialized_view_mv__tag_arrays()
    """

    db = setup_db(appname="Materialze mv__tag_arrays")
    try:
        start_time = time.time()
        db.executesql(
            """
        REFRESH MATERIALIZED VIEW mv__tag_arrays;
        """
        )
        duration = time.time() - start_time
        print(f"materialiation of mv__tag_arrays complete in {duration} seconds")
        db.commit()
    finally:
        db.close()


@scheduler.task(bind=True, max_retries=int(required_env("UPLOAD_MAX_RETRIES")))
def upload_attachment(self, gid: UUID, filename: str, content: str):
    try:
        fd, tempfilename = tempfile.mkstemp(suffix=Path(filename).suffix)
        print(f"Using {tempfilename} as tempfile.")
        os.write(fd, base64.b64decode(content))
        os.close(fd)

        new_filename = str(gid) + Path(filename).suffix
        b2 = local["~/.local/bin/b2"]
        cmd = b2[
            "upload-file",
            required_env("B2_ATTACHMENTS_BUCKETNAME"),
            tempfilename,
            new_filename,
        ]
        print(f"Execute {cmd}")
        code, stdout, stderr = cmd.run(retcode=None)

        os.unlink(tempfilename)

        if code == 0:
            # no problems detected
            output_lines = stdout.split("\n")
            url_by_name = output_lines[0]
            # url_by_fileid = output_lines[1]
            # json_data = json.loads("\n".join(output_lines[2:]))
            b2_uri = url_by_name.split(":", maxsplit=1)[1].strip()
            # upload completed succesfully

            # save the url to database
            db = setup_db_tables(setup_db(appname="Upload Attachment"))
            attachment = db.attachment(gid=gid)
            updated = attachment.update_record(b2_uri=b2_uri)
            db.commit()
            db.close()
            onbekend(
                f"Uploaden van {new_filename} gelukt, URL bijgewerkt in de database."
            )
        else:
            # on error continue
            b2_uri = None
            print("B2 stdout:", stdout)
            print("B2 stderr:", stderr)
            error(f"Uploaden van {new_filename} mislukt.\n\n{stderr}")
            raise ValueError(f"Problem uploading attachment to b2: {gid}")
    except Exception as e:
        print(e)
        self.retry(
            countdown=eval(
                required_env("UPLOAD_NEXT_RETRY_DELAY_EXPRESSION"),
                dict(),
                dict(retries=self.request.retries),
            )
        )
        raise


@scheduler.task(bind=True)
def update_opengraph_all(self):
    db = setup_db_tables(setup_db(appname="Update Opengraph Metadata"))
    dc = opengraph.DiskCacher(db)
    return dc.update_all()


@scheduler.task(bind=True)
def update_opengraph_by_gid(self, gid: UUID):
    db = setup_db_tables(setup_db(appname="Update Opengraph Metadata"))
    dc = opengraph.DiskCacher(db)
    return dc.update_by_gid(gid)


@scheduler.task(bind=True, max_retries=0, ignore_result=True)
def shutdown_workers(self):
    """
    Shuts down the workers.

    This function broadcasts a shutdown command to all workers using `scheduler.control.broadcast("shutdown")`.
    It also purges any pending tasks using `scheduler.control.purge()`.
    """
    scheduler.control.broadcast("shutdown")
    scheduler.control.purge()


@scheduler.task
def work_auto_tags_magic():
    env = Environment()
    db = env.db
    backend = env.backend
    visibilities_by_value = {v.value: v for v in Visibility}
    update_materialized_view_mv__item_tags()
    try:
        dirty = False
        for auto_tag_record in db(db.auto_tag).select():
            # for each query record find the currently tagged items with the destination tag
            tagged_in_db = set(
                db(db.mv__item_tags.tag_gid == auto_tag_record.tag_gid)
                .select(db.mv__item_tags.item_gid)
                .column("item_gid")
            )
            # find the query results based on the materialized view and query stuff
            visibilities = [
                visibilities_by_value[v] for v in auto_tag_record.visibilities
            ]
            search_results = set(
                backend.search_items(
                    None,
                    search=auto_tag_record.needle,
                    first=None,
                    included_visibilities=visibilities,
                ).found
            )
            # update the in memory database to show the stats
            auto_tag_record.update_record(
                tagged_in_db=list(tagged_in_db), search_results=list(search_results)
            )
            diff = search_results - tagged_in_db
            print(
                f"{auto_tag_record.needle} w/ {visibilities}: "
                f"{len(diff)} new: {diff}, total found: {len(search_results)}. "
                f"New applied: {diff}"
            )
            db.commit()

            # do the math: remove the tags from those items that are tagged and should not be tagged based on query results
            # untag_these_items = tagged_in_db - search_results
            # in reverse: for the items that should be tagged, but arent: add the tag.
            add_tags_to_these_items = diff

            # print("--", untag_these_items)
            # print("++", add_tags_to_these_items)

            # not going to remove possibly manually assigned (sticker)tags.
            # for item_gid in untag_these_items:
            #     record = database.item(gid=item_gid)
            #     record.update_record(
            #         tags=list(set(record.tags) - {auto_tag_record.tag_gid})
            #     )
            for item_gid in add_tags_to_these_items:
                record = db.item(gid=item_gid)
                record.update_record(
                    tags=list(set(record.tags + [auto_tag_record.tag_gid]))
                )
            dirty = dirty or add_tags_to_these_items  # or untag_these_items
        if dirty:
            db.commit()
            update_materialized_view_mv__item_tags.delay()
            return "dirty, marked mv__item_tags for update"
        return "clean"

    except Exception as e:
        print("work_auto_tags_magic failed:", e)
        db.rollback()
        return f"Error: {e}"


# run my_task every 10 seconds
scheduler.conf.beat_schedule = {
    "update_materialized_view_mv__item_tags": {
        "task": "edwh.core.backend.tasks.update_materialized_view_mv__item_tags",
        "schedule": 60 * 10,
        "args": (),
    },
    "update_materialized_view_mv__tag_arrays": {
        "task": "edwh.core.backend.tasks.update_materialized_view_mv__tag_arrays",
        "schedule": 60 * 10,
        "args": (),
    },
    "update_opengraph_all": {
        "task": "edwh.core.backend.tasks.update_opengraph_all",
        "schedule": 3600,  # todo: change?
        "args": (),
    },
    "shutdown_workers": {
        "task": "edwh.core.backend.tasks.shutdown_workers",
        "schedule": 3600,  # restart every hour to prevent database connection leaks.
        "args": (),
    },
    "work_auto_tags_magic": {
        "task": "edwh.core.backend.tasks.work_auto_tags_magic",
        "schedule": 600,  # fix every 10 minutes
        "args": (),
    },
}
