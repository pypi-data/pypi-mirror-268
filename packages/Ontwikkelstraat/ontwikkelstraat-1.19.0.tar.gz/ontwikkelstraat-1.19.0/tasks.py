import datetime
import glob
import json
import os
import pathlib
import random
import sys
import warnings
from pathlib import Path

# end stdlib, start try:

try:
    import edwh
    import edwh.tasks  # stupide pycharm!
    import tomlkit
    from edwh.tasks import DOCKER_COMPOSE
    from invoke import Context, Result, run, task
    from termcolor import colored


except ImportError as import_err:
    if sys.argv[0].split("/")[-1] in ("inv", "invoke"):
        print(
            "WARNING: this tasks.py works best using the edwh command instead of using inv[oke] directly."
        )
        print("Example:")
        if sys.argv[1].startswith("-"):
            print("> edwh", " ".join(sys.argv[1:]))
        else:
            print("> edwh local." + " ".join(sys.argv[1:]))
        print()

    print(
        "Install edwh using `pipx install edwh[omgeving]` to automatically install edwh and all dependencies."
    )
    print(
        "Or install using `pip install -r requirements.txt` in an appropriate virtualenv when not using edwh. "
    )
    print()
    print("ImportError:", import_err)

    exit(1)

def find_differences_in_dictionaries(
    what_is: dict, what_should_be: dict, prefix: str
) -> bool:
    """Find differences between dicts, useful for testing template keys in a given larger config file.
    Example:
        find_differences_in_dictionaries(
            config["pytest"], template["pytest"], "pytest/"
        )
    """
    found_missing = False
    for key, value in what_should_be.items():
        if key not in what_is:
            found_missing = True
            print(f"Missing: {prefix}/{key}: {value}")
        if isinstance(value, dict):
            # recursively find differences for each dict
            found_missing = found_missing or find_differences_in_dictionaries(
                what_is.get(key, {}),
                what_should_be[key],
                prefix=os.path.join(prefix, key),
            )
    return found_missing


class SomethingWentWrong(Exception):
    pass


def failsafe(c: callable) -> None:
    """Executes the callable, and if not result.ok raises a RemoteWentWrong exception."""
    result: Result = c()
    if not result.ok:
        raise SomethingWentWrong(result.stderr)


class WiseException(EnvironmentError):
    pass


def productie_prompt(prompt):
    with open(".env", "r") as env_file:
        if "meteddie.nl" in env_file.read():
            print("Dit lijkt op een productie machine (meteddie in .venv)")
            choice = input(prompt)
            if choice != "ja":
                print("Verstandig!")

                raise WiseException("Productie database - niet aankomen")


def uptimerobot_autoadd(c: Context) -> None:
    """
    Runs `auto-add` from the edwh-uptime-plugin,
        but only warns if that plugin is not installed (instead of stopping the program via an exception).
    """
    try:
        from edwh_uptime_plugin import tasks as edwh_uptime
    except ImportError:
        warnings.warn(
            "`edwh-uptime-plugin` not installed, can't perform UptimeRobot auto-add."
        )
        return

    edwh_uptime.auto_add(c, quiet=True)


def bundler_build(c: Context) -> None:
    """
    Run `bundle.build` if the edwh-bundler-plugin is installed.
    """

    try:
        from edwh_bundler_plugin import build
    except ImportError:
        warnings.warn(
            "`edwh-bundler-plugin` not installed, can't perform static file building."
        )
        return

    try:
        print("Starting bundle.build")
        build(c)
    except Exception as e:
        # failing build may not hinder the rest of setup
        warnings.warn(f"bundle.build failed ({e})", source=e, category=RuntimeWarning)


@task()
def clean(
    ctx,
    all=False,
    db=False,
    postgres=False,
    redis=False,
):
    """Rebuild the databases, possibly rebuild microservices.

    Execution:
    0. build microservices (all, microservices)
       if force_rebuild:
         does not use docker-image cache, thus refreshing even with the same backend version.
         use this is you wish to rebuild the same backend. Easier and faster to use fix: or perf: in the backend...
    1. stopping postgres instances (all, db, postgres)
    2. removing volumes (all, db, postgres)
    3. rebooting postgres instances (all, db, postgres)
    4. ~~purge redis instances (all, redis)~~ IGNORED

    Removes all ../backend_config/*.complete flags to allow migrate to function properly
    """
    print("-------------------CLEAN -------------------------")
    ctx: Context = ctx
    if all or db or postgres:
        productie_prompt(
            "Weet je zeker dat je de database wilt overschrijven? [ja,NEE]"
        )

        # clear backend flag files
        backend_config = pathlib.Path("../backend_config")
        for flag_file in backend_config.glob("*.complete"):
            print("removing", flag_file)
            flag_file.unlink()

        # find the images based on the instances
        pg_data_volumes = []
        for container_id in (
            ctx.run(f"{DOCKER_COMPOSE} ps -aq pg-0 pg-1 pg-stats", hide=True, warn=True)
            .stdout.strip()
            .split("\n")
        ):
            ran = ctx.run(f"docker inspect {container_id}", hide=True, warn=True)
            if ran.ok:
                info = json.loads(ran.stdout)
                pg_data_volumes.extend([_["Name"] for _ in info[0]["Mounts"]])
            else:
                print(ran.stderr)
                raise EnvironmentError(f"docker inspect {container_id} failed")

        # stop, remove the postgres instances and remove anonymous volumes
        run(f"{DOCKER_COMPOSE} rm -vf --stop pg-0 pg-1 pgpool pg-stats")

        # remove images after containers have been stopped and removed
        print("removing")
        run("docker volume rm " + " ".join(pg_data_volumes), warn=True)
    if redis:
        import redis

        env = edwh.read_dotenv(Path(".env"))
        for db in range(3):
            r = redis.Redis("localhost", int(env["REDIS_PORT"]), db)
            print(f"Removing {len(r.keys())} keys")
            for k in r.keys():
                del r[k]
            r.close()


@task(aliases=("whipe-db",))
def wipe_db(ctx: Context, all=False):
    ctx.run(f"{DOCKER_COMPOSE} stop")
    for p in Path("migrate/flags").glob("migrate-*.complete"):
        p.unlink()
    clean(ctx, db=True)
    edwh.tasks.up(ctx, service=["pgpool"])
    # for cnt in range(25, 1, -5):
    #     print("Let postgres initialize ", cnt, "...")
    #     time.sleep(5)
    edwh.tasks.up(ctx, service=["migrate"], tail=True)
    if all:
        edwh.tasks.up(ctx)


@task()
def fix_default_py4web_apps(c: Context):
    c.run(f"{DOCKER_COMPOSE} run py4web py4web setup --yes apps")


@task()
def wb_test(c: Context):
    c.run(f"{DOCKER_COMPOSE} up web2py-workbench-test")


@task()
def save_backup_through_tunnel(
    c: Context, lightweight=True, username="postgres", host="localhost", port=5432
):
    excludes = (
        "--exclude-table=public.evidence "
        "--exclude-table=public.api_activity "
        "--exclude-table=public.signal "
        "--exclude-table=public.event_stream "
        "--exclude-table=public.session"
        if lightweight
        else ""
    )
    ran = c.run(
        f"pg_dump --dbname=backend "
        f"--file=./migrate/data/database_to_restore.sql "
        f"{excludes} "
        f"--username={username} "
        f"--host={host} "
        f"--port={port}",
        echo=True,
    )
    if ran.ok:
        print("Done, use local.wipe-db to restore the database")
    else:
        print("Error, could not save backup to the database_to_restore.sql file ")


@task()
def generate_jwt_key(_, overwrite=False, w2p_app=None):
    if w2p_app:
        warnings.warn(
            "The w2p app option is deprecated, because keys are not web2py-bound anymore!",
            category=DeprecationWarning,
        )

    shared_keys = Path("shared_keys")
    # shared_keys.mkdir(exist_ok=True)

    key_file = shared_keys / "jwt.key"

    if overwrite:
        key_file.unlink(missing_ok=True)

    try:
        private_key = key_file.read_text()
    except FileNotFoundError:
        private_key = random.randbytes(4096).hex()
        key_file.touch()
        key_file.write_text(private_key)

    return private_key


@task()
def setup_smtp(_, dotenv_path: Path):
    is_fake = (
        edwh.check_env(
            "SMTP_FAKE", "0", "Set to 1 if you don't want to use an actual SMTP server."
        )
        == "1"
    )

    if is_fake:
        # not much more to do then
        return

    smtp_server = edwh.check_env(
        "SMTP_SERVER", "educationwarehouse.org:587", "SMTP Server with or without port"
    )

    if ":" in smtp_server:
        server_part, port_part = smtp_server.split(":")
        edwh.set_env_value(dotenv_path, "SMTP_SERVER", server_part)
        edwh.set_env_value(dotenv_path, "SMTP_PORT", port_part)
    else:
        edwh.check_env("SMTP_PORT", "587", "SMTP Port")

    sender = edwh.check_env(
        "SMTP_SENDER", "from@educationwarehouse.org", "Email address to send mail from."
    )
    user = sender.split("@")[0]

    edwh.check_env("SMTP_USER", user, "SMTP Login User")
    edwh.check_env("SMTP_PASSWORD", "", "SMTP Login Password")
    edwh.check_env("SMTP_TLS", "1", "Use (start)TLS? (1 for yunohost)")
    edwh.check_env("SMTP_SSL", "0", "Use SSL? (0 for yunohost)")


@task()
def setup(c: Context):
    """Setup or update the ontwikkel_omgeving environment."""
    # this is the platform-specific setup hook, which is executed after running the global logic of `ew setup`.
    # normally, you would not run `ew local.setup`.
    print("Setting up/updating  ontwikkel_omgeving ...")
    dotenv_path = Path(".env")
    if not dotenv_path.exists():
        dotenv_path.touch()
    # check these options
    hosting_domain = edwh.check_env(
        key="HOSTINGDOMAIN",
        default="localhost",
        comment="hostname like meteddie.nl; edwh.nl; localhost; robin.edwh.nl",
    )
    hosting_name = edwh.check_env(
        key="APPLICATION_NAME",
        default="hetnieuwedelen",
        comment="used for routing traefik. [www.]<applicationname>.<hostingdomain>, "
        "alongside py4web which is also registered.",
    )

    edwh.check_env(
        key="CERTRESOLVER",
        default="default",
        comment="which certresolver to use - default|staging|letsencrypt. See reverse proxy setup for options",
    )
    edwh.set_env_value(
        dotenv_path, "SCHEMA_VERSION", edwh.tasks.calculate_schema_hash()
    )
    edwh.check_env(
        key="WEB2PY_PASSWORD",
        default=edwh.tasks.generate_password(c, silent=True),
        comment="password for web2py",
    )
    edwh.check_env(
        key="LAB_TOKEN",
        default=edwh.tasks.generate_password(c, silent=True),
        comment="jupyter-lab access token",
    )
    edwh.check_env(
        key="PY4WEB_RESTART_SECRET",
        default=edwh.tasks.generate_password(c, silent=True),
        comment="Py4web restart secret, used internally",
    )
    edwh.check_env(
        key="PY4WEB_APPLOG_ID",
        default="PY4WEB_" + hosting_domain.strip().replace(".", "_").upper(),
        comment="Py4web applog key, should registered at applog when transferred over HTTPS.",
    )
    edwh.check_env(
        key="PY4WEB_APPLOG_KEY",
        default=random.randbytes(32).hex(),
        comment="Py4web applog key, should be registered at applog when transferred over HTTPS.",
    )
    edwh.check_env(
        key="WEB2PY_APPLOG_ID",
        default="WEB2PY_" + hosting_domain.strip().replace(".", "_").upper(),
        comment="web2py applog key, should registered at applog when transferred over HTTPS.",
    )
    edwh.check_env(
        key="WEB2PY_APPLOG_KEY",
        default=random.randbytes(32).hex(),
        comment="web2py applog key, should be registered at applog when transferred over HTTPS.",
    )
    edwh.check_env(
        key="TOOLS_APPLOG_ID",
        default="TOOLS_" + hosting_domain.strip().replace(".", "_").upper(),
        comment="migrate applog key, should registered at applog when transferred over HTTPS.",
    )
    edwh.check_env(
        key="TOOLS_APPLOG_KEY",
        default=random.randbytes(32).hex(),
        comment="TOOLS applog key, should be registered at applog when transferred over HTTPS.",
    )
    edwh.check_env(
        key="GHOST_ADMIN_API_KEY",
        default="Get from ghost...",
        comment="Ghost admin API key, if ghost is used in this project ",
    )
    edwh.check_env(
        key="GHOST_CONTENT_API_KEY",
        default="Get from ghost...",
        comment="Ghost CONTENT API key, if ghost is used in this project ",
    )
    edwh.check_env(
        key="EMAIL_VERIFICATION_SEED",
        default=edwh.tasks.generate_password(c, silent=True),
        comment="Seed used for email verification code hashing.",
    )
    edwh.check_env(
        key="DEFAULT_FROM_ADDRESS",
        default=f"{hosting_name}@{hosting_domain}",
        comment="From address for various emails",
    )
    edwh.check_env(
        key="NTFY_ERROR_URL",
        default=f"EDWH-DEV-ERROR-{os.getenv('HOSTNAME')}",
        comment="Ntfy.sh error channel, use EDWH-ERROR-YXFRXYLZRS in production.",
        prefix="https://ntfy.sh/",
    )
    edwh.check_env(
        key="NTFY_WARNING_URL",
        default=f"EDWH-DEV-WARNING-{os.getenv('HOSTNAME')}",
        comment="Ntfy.sh error channel, use EDWH-WARNING-DEELNVOZSHX in production.",
        prefix="https://ntfy.sh/",
    )
    edwh.check_env(
        key="NTFY_SORT_URL",
        default=f"EDWH-DEV-SORTEERHOED-{os.getenv('HOSTNAME')}",
        comment="Ntfy.sh error channel, use EDWH-SORTEERHOED-DIGVFJJWEN in production.",
        prefix="https://ntfy.sh/",
    )
    edwh.check_env(
        key="PROJECT",
        default=os.getcwd().rsplit("/", 1)[-1].replace(".", "-"),
        comment="Name of the current directory (used for docker and traefik prefixes/suffixes, "
        "to make containers unique)",
    )

    edwh.check_env(
        key="REDIS_PORT",
        default=edwh.tasks.next_value(c, "REDIS_PORT", 6379),
        comment="Port to host Redis on. Avoid collisions when using multiple projects, auto-discovered default",
    )
    edwh.check_env(
        key="PGPOOL_PORT",
        default=edwh.tasks.next_value(c, "PGPOOL_PORT", 5432),
        comment="Port to host pgpool on. Avoid collisions when using multiple projects, auto-discovered default",
    )
    edwh.check_env(
        key="PGSTATS_PORT",
        default=edwh.tasks.next_value(c, "PGSTATS_PORT", 4000),
        comment="Port to host pgpool on. Avoid collisions when using multiple projects, auto-discovered default",
    )
    edwh.check_env(
        key="B2_ATTACHMENTS_BUCKETNAME",
        default="nl-meteddie-delen-attachments",
        comment="Backblaze B2 bucket to store attachments",
    )
    edwh.check_env(
        key="B2_ATTACHMENTS_KEYID",
        default="0030834038a6da40000000001",
        comment="Keyid of the Backblaze b2",
    )
    edwh.check_env(
        key="B2_ATTACHMENTS_KEY",
        default="K00xxxxxxxxxxxxxxxxxxxxxxxNMs",
        comment="Secret key for given backblaze account",
    )
    edwh.check_env(
        key="MAILGUN_DOMAIN",
        default="mg.edwh.nl",
        comment="Mailgun url to send email, used to craft https://api.mailgun.net/v3/MAILGUN_DOMAIN/messages",
    )
    edwh.check_env(
        key="MAILGUN_API_KEY",
        default="bd1xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx31a",
        comment="Mailgun API authentiation",
    )
    edwh.check_env(
        key="MAILGUN_NEXT_RETRY_DELAY_EXPRESSION",
        default="10",
        comment="Mailgun API authentiation, '10' for dev, '1.7**retries' in production",
    )
    edwh.check_env(
        key="MAILGUN_MAX_RETRIES",
        default="15",
        comment="Max retries per Mailgun job, 100 for dev, 20 in production",
    )
    edwh.check_env(
        key="UPLOAD_MAX_RETRIES",
        default="100",
        comment="Max retries per upload job, 100 for dev, maybe even more in production",
    )
    edwh.check_env(
        key="UPLOAD_NEXT_RETRY_DELAY_EXPRESSION",
        default="1.3**retries",
        comment="Max retries per Mailgun job, 100 for dev, 20 in production",
    )
    edwh.check_env(
        key="DOCKER_TAG",
        default="latest",
        comment="'latest' in ontwikkeling, 'PRD' in productie. ",
    )
    edwh.check_env(
        key="PY4WEB_REPLICAS",
        default="3",
        comment="1 in ontwikkeling, 3 in productie. ",
    )
    edwh.check_env(
        key="PY4WEB_DEBUG_MODE",
        default="1",
        comment="'1' in ontwikkeling, '0' in productie. ",
    )
    edwh.check_env(
        key="EMAIL_VALIDATION_JWT_SECRET",
        default=edwh.tasks.generate_password(c, silent=True),
        comment="Password used to sign the email validation JWT in the claim process. ",
    )
    edwh.check_env(
        key="EDDIE_EMAIL",
        default="eddie@edwh.nl",
        comment="Email address of the eddie shared inbox for notifications, "
        "use your own in development or eddie@educationwarehouse.nl in production. ",
    )

    edwh.check_env(
        key="REDASH_SECRET",
        default=edwh.tasks.generate_password(c, silent=True),
        comment="HTTP Basic Auth Password for Redash",
    )

    default_py4web_app = edwh.check_env(
        key="DEFAULT_PY4WEB_APP",
        default="cmsx",
        comment="name of the app in py4web/apps to use as _default",
    )

    setup_smtp(c, dotenv_path)

    uptimerobot_autoadd(c)
    bundler_build(c)

    # make sure the [backup|restore]_stream.sh files in captain-hooks folder exists
    # for easier backup using edwh-restic-plugin
    Path("captain-hooks").mkdir(exist_ok=True)

    if not (backup_script := Path("captain-hooks/backup_stream.sh")).exists():
        backup_script.write_text(
            "#!/bin/bash"
            "docker compose run -T --rm migrate "
            "pg_dump --format=p --dbname=backend --clean --create -h pgpool -U postgres |"
            "restic $HOST -r $URI backup --tag stream --stdin --stdin-filename postgres.sql"
        )
    if not (restore_script := Path("captain-hooks/restore_stream.sh")).exists():
        restore_script.write_text(
            "#!/bin/bash\n"
            "restic $HOST -r $URI dump $SNAPSHOT --tag stream postgres.sql "
            "> ./migrate/data/database_to_restore.sql"
        )
    if not Path("password.txt").exists():
        password = input(
            "Py4web password (blank generates random): "
        ).strip() or edwh.tasks.generate_password(c, silent=True)
        c.run(f"pipx run py4web set_password --password {password}")
        edwh.set_env_value(Path(".env"), "PY4WEB_PASSWORD", password)
        print(f'Password set to: "{password}", keep it safe!')
    else:
        print(
            "Py4web password already set, rm password.txt to update/generate a new password. "
        )
    # add the databases folder for the web2py workbenchs application if it doesn't exists
    if not (databases := Path("web2py/apps/workbench/databases")).exists():
        databases.mkdir()

    # add the reloader file if it doesn't exist.
    if not (reloader_file := Path("py4web/reload.py4web.uwsgi")).exists():
        reloader_file.touch()

    # set the right owner so microservices can edit the flags
    c.sudo("chown -R 1050:1050 migrate/flags")

    print("setting file and directory permissions")
    # set the right owner so microservices can read en edit the apps folder
    edwh.tasks.set_permissions(c, "py4web/apps")
    edwh.tasks.set_permissions(c, "py4web/celery-db")

    # set the right owner so microservices can read en edit the apps folder
    edwh.tasks.clean_old_sessions(c, "web2py/apps/*/sessions")
    edwh.tasks.set_permissions(c, "web2py/apps")

    # set the permissions for these special folders
    edwh.tasks.set_permissions(
        c, "shared_cache", filepermissions=666, directorypermissions=777
    )
    edwh.tasks.set_permissions(c, "shared_applog")

    # install restic
    c.sudo("apt install -y restic")

    if (
        (not Path("./py4web/apps/_dashboard").exists())
        and Path("./migrate/flags/").glob("migrate=-*.complete")
        and edwh.confirm(
            "_dashboard app not found while migrate has run. Want to add the py4web default apps? [yN]"
        )
    ):
        fix_default_py4web_apps(c)

    if default_py4web_app != "_default":
        # only touch the default app if it isn't set to _default in config!
        current_default = Path("./py4web/apps/_default")
        if not current_default.is_symlink():
            if current_default.exists():
                current_default.rename(
                    f"{str(current_default)}.{str(datetime.datetime.now())}.bak"
                )

            current_default.symlink_to(default_py4web_app)

    generate_jwt_key(c)
    print("Use `ew up` to start docker containers.")


@task()
def touch_py4web(ctx: Context):
    # automatische restart via touch file
    ctx.run("touch py4web/reload.py4web.uwsgi")

@task()
def shrink_database_for_development(ctx: Context):
    productie_prompt(
        "Weet je zeker dat je de data wil verwijderen om de database compact te maken? [ja,NEE]"
    )
    print("Stopping celeries")
    edwh.tasks.stop(ctx, service=["celery*"])
    print("Calling migrate to prune")
    ctx.run(
        f"{DOCKER_COMPOSE} run --rm migrate "
        "invoke "
        "-r /shared_code/edwh/core/backend "
        "-c support "
        "shrink-database-for-development"
    )
    print("Restarting celeries")
    edwh.tasks.up(ctx, service=["celery*"])


@task()
def table_sizes(ctx: Context):
    ctx.run(
        f"{DOCKER_COMPOSE} run --rm migrate invoke -r /shared_code/edwh/core/backend -c support show-table-sizes"
    )


@task()
def cache_info(ctx: Context):
    ctx.run(
        f"{DOCKER_COMPOSE} run --rm migrate invoke -r /shared_code/edwh/core/backend -c support cache-info"
    )


@task()
def cache_size(ctx: Context):
    ctx.run(
        f"{DOCKER_COMPOSE} run --rm migrate invoke -r /shared_code/edwh/core/backend -c support cache-size"
    )


@task()
def database_connections(ctx: Context):
    """Show current database connections, does require a new connection."""
    ctx.run(
        f"{DOCKER_COMPOSE} run --rm migrate invoke -r /shared_code/edwh/core/backend -c support database-connections"
    )


@task()
def uncache(ctx: Context):
    ctx.run(
        f"{DOCKER_COMPOSE} run --rm migrate python3 /shared_code/edwh/core/pgcache/clean.py"
    )


@task()
def set_password(ctx: Context, email: str, password: str=None):
    if not password:
        import getpass
        password = getpass.getpass("password to set (asked to prevent echoing): ")

    ctx.run(
        f"{DOCKER_COMPOSE} run --rm migrate "
        f"invoke "
        f"-r /shared_code/edwh/core/backend "
        f"-c support "
        f"set-password "
        f"--email {email} "
        f"--password {password}"
    )


@task()
def monitor_applog(ctx: Context, n=10):
    ctx.run(
        f"{DOCKER_COMPOSE} run --rm migrate invoke -r /shared_code/edwh/core/backend -c support monitor-applog -n {n}"
    )


@task()
def invoke_cli_support(_: Context):
    print(
        f"{DOCKER_COMPOSE} run --rm migrate invoke -r /shared_code/edwh/core/backend -c support <regular invoke cmdline> "
    )


@task()
def up(ctx: Context, services: list[str]):
    # this is the platform-specific up hook, which is executed after running the global logic of `ew up`.
    # normally, you would not run `ew local.up`.
    if "py4web" in services:
        print("Updating opengraph metadata")
        ctx.run(
            f"{DOCKER_COMPOSE} run --rm migrate invoke -r /shared_code/edwh/core/backend -c support update-opengraph",
            warn=True,
        )


@task()
def clean_jupyter(ctx: Context, notebook: str = "", notebooks: glob.glob = "", yes=False):
    """
    Clean the output of one or more jupyter notebooks

    'notebook' and 'notebooks' are aliases, both work the same way (with a glob) -
    *.ipynb will clean all notebooks in 'work' (= ./jupyterlab/notebooks)
    """

    if not (notebook or notebooks):
        print("Please provide either --notebook or --notebooks")
        exit(1)

    _host_path = "jupyterlab/notebooks"
    _docker_path = "work"

    selected_files = []

    if notebook:
        notebook = notebook.removeprefix(_host_path)
        selected_files += glob.glob(f"{_host_path}/{notebook}")

    if notebooks:
        notebooks = notebooks.removeprefix(_host_path)
        selected_files += glob.glob(f"{_host_path}/{notebooks}")

    print("The following files will be cleaned:")
    for file in set(selected_files):
        print("-", file.split("/")[-1])

    if yes or edwh.confirm("Do you want to clean these files? [yN] "):
        clean = f"{DOCKER_COMPOSE} run jupyterlab jupyter nbconvert --clear-output --inplace"

        if notebooks:
            ctx.run(f"{clean} work/{notebooks}")

        if notebook:
            ctx.run(f"{clean} work/{notebook}")

        print()
        print(colored(f"✓ Cleaned {len(selected_files)} files.", "green"))


@task()
def pip_bump_all(c: Context):
    """
    Bump all .txt files using `edwh pip.upgrade`.

    All used is:
        - web2py
        - py4web
        - migrate
        - jupyterlab
    """
    c.run("edwh pip.upgrade web2py,py4web,jupyterlab,migrate")


@task()
def migrate(ctx):
    edwh.tasks.up(ctx, service=["migrate"], tail=True)
