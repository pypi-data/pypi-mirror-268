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
from pydal import DAL

from .common import fragmentx_scheduler as scheduler

# from edwh.core.backend.ntfy_sh import error, warning
# from ycecream import y
# from attrs import define, field
Row = DAL.Row

# # example of task that needs db access


# @scheduler.task
# def my_task():
#     try:
#         # this task will be executed in its own thread, connect to db
#         db._adapter.reconnect()
#         # do something here
#         db.commit()
#     except:
#         # rollback on failure
#         db.rollback()


@scheduler.task
def log_once(who=None):
    # usage: log_once.delay()

    # this task will be executed in its own thread, connect to db
    # db._adapter.reconnect()

    if not who:
        who = "World"
    print(f"Hello {who}")


# @scheduler.task
# def log_often():
#     print("Hello Again")
#
# # run my_task every 10 seconds
# scheduler.conf.beat_schedule = {
#     "my_first_task": {
#         "task": "apps.%s.tasks.log_often" % settings.APP_NAME,
#         "schedule": 10.0,
#         "args": (),
#     },
# }
