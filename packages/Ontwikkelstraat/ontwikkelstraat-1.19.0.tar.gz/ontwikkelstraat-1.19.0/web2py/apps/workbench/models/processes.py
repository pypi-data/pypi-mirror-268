import os
import pathlib
import signal


def restart_py4web():
    print(os.getpid())
    print("toedels!")
    os.kill(os.getpid(), signal.SIGKILL)
    session.flash = "Herstart aangevraagd py4web, dit kan een paar seconden duren. "
