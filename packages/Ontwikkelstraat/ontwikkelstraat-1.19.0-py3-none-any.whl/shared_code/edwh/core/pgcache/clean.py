import edwh_migrate


def clean():
    """Clean the cache of the database designated through environment variable $POSTGRES_URI.

    Uses edwh.core.migrate.setup_db for connection
    """
    print("Connecting to database ...")
    db = edwh_migrate.setup_db(appname="clean cache")
    print("Connected, truncating ...")
    db.executesql(
        """

    truncate table public.deps; 
    truncate table public.cache; 

    """
    )
    db.commit()
    print("done. ")


if __name__ == "__main__":
    clean()
