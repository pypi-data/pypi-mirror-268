import time

from gluon.scheduler import Scheduler
from ycecream import y


def synchronize(limit, offset):
    """Task to sync items with delen.meteddie.nl"""
    raise RuntimeError(
        "STuk, want ik heb de signatuur van backend.items aangepast en hier nog niet doorgevoerd. "
    )
    # we want to get all of the items from the GraphQL backend.
    start_query = time.time()
    items = backend.items(limit=limit, offset=offset)
    property_bags = {}
    for item in items:
        pbag = backend.property_bag(belongs_to=item["id"])
        property_bags[item["id"]] = pbag.get("bag") if pbag else {}
    y(len(property_bags))
    y(len(items), "from GraphQL")
    y(time.time() - start_query, "seconds taken")
    # we want to get all of the uris from the items.
    uris = [f'https://delen.meteddie.nl/item/{_["id"]}' for _ in items]
    # then see which items are present in the workbench_database.
    query = workbench_db.item.ori_uri.belongs(uris)
    workbench_items = workbench_db(query).select(
        workbench_db.item.raw_text, workbench_db.item.id, workbench_db.item.ori_uri
    )
    y(workbench_items, "present in workbench database.")
    # keep track of the synced gids
    synced_gids = []
    # after that, for each item that is present in the workbench, fetch the item that matches with the uri in GraphQL
    if workbench_items:
        for wb_item in workbench_items:
            try:
                # we only need the item that has the same id as the one present in the ori_uri
                item = [_ for _ in items if _.get("id") in wb_item.ori_uri][0]
                if not item:
                    raise BackendError(
                        "Geen item gevonden. die matcht met ", wb_item.ori_uri
                    )
                short_description = item.get("shortDescription", "")
                this_property_bag = property_bags[item.get("id")]

                # compare the old raw_text to the one fetched from the GraphQL backend.
                old = (
                    "".join(_ for _ in wb_item.raw_text.splitlines(True))
                    if wb_item.raw_text
                    else ""
                )
                new = (
                    "".join(_ for _ in short_description.splitlines(True))
                    if short_description
                    else ""
                )
                if old != new:
                    add_comment(
                        "item",
                        wb_item.id,
                        f"item synchronisatie vanaf delen.meteddie.nl.",
                    )
                    new = html2markdown.convert(new) if new else ""
                    # update the item to become the shortDescription of Eddie item.
                    wb_item.update_record(
                        raw_text=new, title=item["name"], property_bag=this_property_bag
                    )

                synced_gids.append(item.get("id"))
            except BackendError:
                raise BackendError("Something went wrong.")
            except Exception as e:
                y(e)
                raise
    new_items = []
    for item in items:
        try:
            if item["id"] in synced_gids:
                pass
            else:
                # this means the item has not been synced, it probably doesn't exist in the database.
                new_item = generic_importer(
                    contact_id=None,
                    title=item["name"],
                    raw=item["shortDescription"],
                    ori_uri=f'https://delen.meteddie.nl/item/{item["id"]}',
                    attachments=item["attachments"],
                    tag_gids=[_["id"] for _ in item["tags"]],
                    comment="item geïmporteerd gedurende de synchronisatie.",
                    property_bag=property_bags[item.get("id")],
                )
                new_items.append(new_item)
                synced_gids.append(item.get("id"))
        except Exception as e:
            y(e)
            raise
    y(len(new_items), "new items found")
    y(len(synced_gids), "items synced")


def task_eddie_sync():
    y("worker | starting synchronization with eddie...")
    t0 = time.time()
    available = backend.available_items()
    y(available)
    per_batch = 10
    for start in range(0, available, per_batch):
        synchronize(limit=per_batch, offset=start)
    y("worker | sync done")
    y(time.time() - t0, "seconds taken")


scheduler = Scheduler(db, tasks=dict(sync_eddie=task_eddie_sync))
