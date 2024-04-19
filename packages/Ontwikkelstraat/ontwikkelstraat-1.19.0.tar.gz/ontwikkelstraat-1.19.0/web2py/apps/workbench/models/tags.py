from edwh.core.tags import *


def bind_attachment_and_sticker(db, tag_gid, attachment_gid):
    db.sticker.update_or_insert(
        db.sticker.tag_gid == tag_gid,
        tag_gid=tag_gid,
        attachment_gid=attachment_gid,
    )


def unbind_sticker(db, tag_gid):
    """Removes a sticker from a tag. Keeps the tag intact, does not remove the attachment."""
    db(db.sticker.tag_gid == tag_gid).delete()


def create_new_sticker_tag(name):
    tag = None
    with contextlib.suppress(Exception):
        tag = Tag(name)
    if tag:
        raise ValueError(f'Tag "{name}" already used.')
    sticker = Tag.new(name, name, parents=[Tag("Stickers")], meta_tags=[TSystem])
    return sticker.gid
