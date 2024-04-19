# py4web_wsgi.py
# https://py4web.com/_documentation/static/en/chapter-03.html#wsgi
import os
import time

import bjoern
import watchdog.events
import watchdog.observers

from py4web.core import wsgi

# class ReloadException(Exception):
#     pass
#
#
# # add a watchdog observer to reload the app when a file changes
# class ReloadHandler(watchdog.events.FileSystemEventHandler):
#     def on_any_event(self, event):
#         print("Reloading py4web apps in watchdog handler", event)
#         raise ReloadException()
#
#
# if patterns := os.getenv("BJOERN_RESTART_ON_FILE_CHANGE", ""):
#     print("ENABLING bjoern restart on file change on ", patterns)
#     observer = watchdog.observers.Observer()
#     observer.schedule(
#         ReloadHandler(),
#         "/p4w/reload.py4web.uwsgi",
#         recursive=False,
#     )
#     observer.start()
# else:
#     print("NOT ENABLING bjoern restart on file change")

# https://py4web.com/_documentation/static/en/chapter-03.html#debugging
if os.getenv("DEBUG_PYCHARM_WITH_BJOERN", "").lower().strip() == "true":
    import pydevd_pycharm

    pydevd_pycharm.settrace(
        "host.docker.internal",
        port=12321,
        stdoutToServer=False,
        stderrToServer=False,
        suspend=False,
    )
if __name__ == "__main__":
    application = wsgi(apps_folder="apps")
    bjoern.run(application, "0.0.0.0", 8000)
