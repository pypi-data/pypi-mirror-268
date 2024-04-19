import os

# general settings
APP_FOLDER = os.path.dirname(__file__)

# session settings
SESSION_TYPE = "redis"
SESSION_SECRET_KEY = "0e1d4ad8-4c5f-4f54-bf65-a1ac8ec1a36f"  # replace this with a uuid
MEMCACHE_CLIENTS = ["127.0.0.1:11211"]
REDIS_SERVER = f"{os.environ['REDIS_MASTER_HOST']}:6379"
