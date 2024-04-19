import os

from py4web import action, request

print(
    "RESTART uri:",
    f"https://{os.environ['APPLICATION_NAME']}.{os.environ['HOSTINGDOMAIN']}/restart/index/{os.environ['PY4WEB_RESTART_SECRET']}",
)


@action("index/<secret>")
@action("index")
def index(secret=None):
    data = request.query or request.forms or request.json

    secret = secret or data.get("secret")

    # [Code in workbench voor hetstarten server wijzigen:#44@EWCore](https://taiga.edwh.nl/project/remco-ewcore/task/44)
    if secret == os.environ["PY4WEB_RESTART_SECRET"]:
        # print("touching /p4w/reload.py4web.uwsgi")
        # # alleen Path.touch() is niet genoeg, want die touched niet echt, die maakt alleen nieuwe files aan.
        # with pathlib.Path("/p4w/reload.py4web.uwsgi").open(mode="w") as touch_file:
        #     touch_file.write(
        #         f"Restart requested at {datetime.datetime.now().isoformat()}"
        #     )
        # terminate the process
        os.kill(os.getpid(), 15)  # 15 is SIGTERM
        # this will never be reached
        return "Restart requested"
    else:
        print("invalid secret received")
        return "invalid secret"
