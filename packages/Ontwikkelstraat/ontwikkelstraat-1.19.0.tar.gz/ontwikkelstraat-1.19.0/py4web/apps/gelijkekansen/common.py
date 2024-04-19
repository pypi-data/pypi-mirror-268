import redis

from py4web import Cache, Session

from . import settings

host, port = settings.REDIS_SERVER.split(":")
# for more options: https://github.com/andymccurdy/redis-py/blob/master/redis/client.py
conn = redis.Redis(host=host, port=int(port))
conn.set = (
    lambda k, v, e, cs=conn.set, ct=conn.ttl: cs(k, v, ct(k))
    if ct(k) >= 0
    else cs(k, v, e)
)
session = Session(secret=settings.SESSION_SECRET_KEY, same_site="None", storage=conn)

cache = Cache(size=1000)
