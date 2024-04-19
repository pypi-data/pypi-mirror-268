"""
This is an optional file that defined app level settings such as:
- database settings
- session settings
- i18n settings
This file is provided as an example:
"""
import os

from py4web.core import required_folder

# db settings
APP_FOLDER = os.path.dirname(__file__)
APP_NAME = os.path.split(APP_FOLDER)[-1]
# DB_FOLDER:    Sets the place where migration files will be created
#               and is the store location for SQLite databases

# normal:
DB_FOLDER = required_folder(APP_FOLDER, "databases")
DB_URI = os.environ["POSTGRES_URI"]
DB_POOL_SIZE = 1  # BJOERN: 1 anders 10
DB_MIGRATE = False
DB_FAKE_MIGRATE = False  # maybe?

# LTS specific:
LTS_ASSETS_DB_FOLDER = "/tmp"  # required_folder(APP_FOLDER, "databases")
LTS_ASSETS_NAME = "lts_assets"
LTS_ASSETS_DB_URI = f"sqlite://{LTS_ASSETS_NAME}.db"
LTS_ASSETS_DB_POOL_SIZE = 1
LTS_ASSETS_DB_MIGRATE = True
LTS_ASSETS_DB_FAKE_MIGRATE = False  # maybe?

# LTS specific:
LTS_USERS_DB_FOLDER = required_folder(APP_FOLDER, "databases")
LTS_USERS_DB_URI = "sqlite://lts_users.db"
LTS_USERS_DB_POOL_SIZE = 1
LTS_USERS_DB_MIGRATE = True
LTS_USERS_DB_FAKE_MIGRATE = False  # maybe?

# location where static files are stored:
STATIC_FOLDER = required_folder(APP_FOLDER, "static")

# location where to store uploaded files:
UPLOAD_FOLDER = required_folder(APP_FOLDER, "uploads")

# send email on registration
VERIFY_EMAIL = False

# account requires to be approved ?
REQUIRES_APPROVAL = False

# ALLOWED_ACTIONS:
# ["all"]
# ["login", "logout", "request_reset_password", "reset_password", "change_password", "change_email", "update_profile"]
# if you add "login", add also "logout"
# ALLOWED_ACTIONS = ["all"]
ALLOWED_ACTIONS = [
    "login",
    "logout",
    # "register",
]  # add/remove register depending on whether it is dev or prod?

# email settings
SMTP_SERVER = "smtp.eu.mailgun.org:465"
SMTP_SENDER = os.environ.get("LTS_EMAIL_NOTIFICATION_SENDER")
SMTP_LOGIN = os.environ.get("LTS_EMAIL_NOTIFICATION_LOGIN")
SMTP_TLS = True
SMTP_SSL = True

# session settings
SESSION_TYPE = "redis"
SESSION_SECRET_KEY = "0e1d4ad8-4c5f-4f54-bf65-a1ac8ec1a36f"  # replace this with a uuid
MEMCACHE_CLIENTS = ["127.0.0.1:11211"]
REDIS_SERVER = f"{os.environ['REDIS_MASTER_HOST']}:6379"

# logger settings
LOGGERS = [
    "warning:stdout"
]  # syntax "severity:filename" filename can be stderr or stdout

# single sign on Google (will be used if provided)
OAUTH2GOOGLE_CLIENT_ID = None
OAUTH2GOOGLE_CLIENT_SECRET = None

# single sign on Okta (will be used if provided. Please also add your tenant
# name to py4web/utils/auth_plugins/oauth2okta.py. You can replace the XXX
# instances with your tenant name.)
OAUTH2OKTA_CLIENT_ID = None
OAUTH2OKTA_CLIENT_SECRET = None

# single sign on Google (will be used if provided)
OAUTH2FACEBOOK_CLIENT_ID = None
OAUTH2FACEBOOK_CLIENT_SECRET = None

# enable PAM
USE_PAM = False

# enable LDAP
USE_LDAP = False
LDAP_SETTINGS = {
    "mode": "ad",
    "server": "my.domain.controller",
    "base_dn": "ou=Users,dc=domain,dc=com",
}

# i18n settings
T_FOLDER = required_folder(APP_FOLDER, "translations")

# Celery settings
USE_CELERY = True
CELERY_BROKER = "redis://localhost:6379/0"

# try import private settings
try:
    from .settings_private import *
except (ImportError, ModuleNotFoundError):
    pass
