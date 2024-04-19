import base64
import datetime
import uuid

from edwh.core.data_model import setup_db_tables
from edwh_migrate import setup_db

from py4web import action, redirect
from py4web.core import DAL

# db is pydal.DAL now by default,
# but py4web requires slightly different (patched) DAL to function
# (py4web.core.dal which extends Fixture and pydal.DAL to work ThreadSafe)
db = setup_db_tables(setup_db(appname="Click tracker", dal_class=DAL))


def unshorten_gid(permalink_code: str) -> uuid.UUID:
    """Unshorten the string representation to a uuid.UUID object."""
    return uuid.UUID(bytes=base64.b64decode(permalink_code + "======", "+_"))


def translate_shorturl(session_gid_hash, permalink_item_code, shortcode, timestamp):
    """Returns long URL and saves the timestamp for stats on item_gid and short_url"""
    # save request
    db.click__event.insert(
        short_code=shortcode,  # save as reference to the url
        session_gid_hash=session_gid_hash,  # save as is, since it's a hash
        from_item_gid=unshorten_gid(permalink_item_code),
        ts=timestamp,
    )
    # return long url
    record = (
        db(db.click__url.short_code == shortcode).select(db.click__url.long_url).first()
    )
    db.commit()
    if not record:
        raise ValueError(f"404: No URL found for {shortcode}")

    long_url = record.long_url
    if not long_url.startswith(("http://", "https://")):
        long_url = f"http://{long_url}"

    return long_url


@action("<ignored>/<permalink>/<shortcode>")
@action.uses(db)
def c(ignored, permalink, shortcode):
    long_url = translate_shorturl(
        ignored, permalink, shortcode, datetime.datetime.now()
    )
    return redirect(long_url)


@action("index")
def index():
    return "Hello World, this is your friendly clicktracker."
