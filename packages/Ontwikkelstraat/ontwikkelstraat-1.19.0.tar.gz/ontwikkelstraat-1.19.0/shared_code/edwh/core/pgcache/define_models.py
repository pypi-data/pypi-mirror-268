from pydal import Field


def define_model(db):
    db.define_table(
        "cache",
        Field("gid", "string"),
        Field("value", "blob"),
        Field("ttl", "integer"),
        Field(
            "expired", "boolean"
        ),  # niet echt, deze wordt alleen gebruikt voor een virtueel veld.
    )
    db.define_table(
        "deps",
        Field(
            "cache_id",
            "reference cache",
        ),
        Field("depends_on", "reference cache"),
    )
    return db
