import json
import typing

if typing.TYPE_CHECKING:
    from gluon import HTTP, auth, request
    from pydal import DAL
    from ycecream import y

    from ..models.db_workbench import workbench_db
    from ..models.db_z_backend import backend

    db: DAL
    database: DAL


@auth.requires_login()
def workbench_item_tag():
    """Bedoeld om tags aan een item toe te voegen, of te verwijderen.

    :return: HTTP object.
    """
    if not request.method == "POST":
        return HTTP(405)
    if not backend.token:
        return HTTP(401)

    # TODO: dit via request.post_vars doen. dit betekent dat de AJAX call aangepast moet worden.
    # TODO: dit betekent ook gelijk dat er delen van deze functie aangepast moeten worden.
    item_id = request.vars.get("item_id")
    tags = request.vars.get("tags")

    if not item_id:
        return HTTP(400)

    if isinstance(tags, str):
        # we willen hier een lijst van tags van maken,
        # bij een POST met ajax worden de waarden namelijk gescheiden door een `,`
        tags = [_.split(":")[-1] for _ in tags.split(",")]
    elif isinstance(tags, list):
        tags = [_.split(":")[-1] for _ in tags]

    cur_tags = workbench_db(workbench_db.item_tag.item_id == item_id).select().as_list()
    # alle gids van de huidige gekoppelde tags van dit item.
    cur_tags = [_["tag_gid"] for _ in cur_tags]
    if sorted(cur_tags) != sorted(tags):
        for tag in tags:
            if tag in cur_tags:
                pass
            else:
                workbench_db.item_tag.insert(item_id=item_id, tag_gid=tag)

        if cur_tags:
            to_delete = []
            for tag in cur_tags:
                if tag not in tags:
                    to_delete.append(tag)
            if to_delete:
                query = (
                    """DELETE FROM item_tag WHERE tag_gid IN %s AND item_id = %s"""
                    % (
                        tuple(to_delete) if len(to_delete) > 1 else (to_delete[0], ""),
                        item_id,
                    )
                )
                workbench_db.executesql(query)
    return HTTP(200)


@auth.requires_login()
def backend_item_tag():
    """Bedoeld om tags aan een item toe te voegen, of te verwijderen.

    :return: HTTP object.
    """
    if not request.method == "POST":
        return HTTP(405)

    # TODO: dit via request.post_vars doen. dit betekent dat de AJAX call aangepast moet worden.
    # TODO: dit betekent ook gelijk dat er delen van deze functie aangepast moeten worden.
    item_id = request.vars.get("item_id")  # item.id
    tags = request.vars.get("tags")  # list of gids

    if not item_id:
        return HTTP(400)

    if isinstance(tags, str):
        # we willen hier een lijst van tags van maken,
        # bij een POST met ajax worden de waarden namelijk gescheiden door een `,`

        # remove prefix, separated by :
        tags = [_.split(":")[-1] for _ in tags.split(",")]
    elif isinstance(tags, list):
        tags = [_.split(":")[-1] for _ in tags]

    # make unique
    tags = list(set(tags))

    row = (
        database(database.item.id == item_id)
        .select(database.item.id, database.item.gid, database.item.tags)
        .first()
    )
    current_tags = row.tags
    row.update_record(tags=tags)
    database.commit()
    backend.applog.update_item(
        row.gid,
        by_eddie_email=auth.user.email,
        fields_before={"tags": current_tags},
        fields_after={"tags": tags},
    )
    # TODO: message versturen dat bijwerken van de tags gedaan kan worden in de achtergrond.
    return HTTP(200)


@auth.requires_membership("education_warehouse")
def update_tags():
    if not request.method == "POST":
        return HTTP(405)
    if not backend.token:
        return HTTP(401)

    data = request.post_vars["data"]
    # data is hier een JSON string
    data = json.loads(data)
    y(data)
    tags = data.keys()
    for tag in tags:
        record = database.tag(gid=tag)
        new_parent = data[tag]["new_parent"]
        old_parent = data[tag]["old_parent"]
        if new_parent in record.parents:
            pass
        record_parents = record.parents
        y(record.parents)
        if old_parent in record_parents:
            record_parents.remove(old_parent)
            record_parents.insert(0, new_parent)
            record.update_record(parents=record_parents)
