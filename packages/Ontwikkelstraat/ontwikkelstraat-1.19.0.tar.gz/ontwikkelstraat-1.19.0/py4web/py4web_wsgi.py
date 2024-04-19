# py4web_wsgi.py
# https://py4web.com/_documentation/static/en/chapter-03.html#wsgi

from py4web.core import Reloader, wsgi

application = wsgi(apps_folder="apps")
# try lazy reloading
Reloader.install_reloader_hook()
