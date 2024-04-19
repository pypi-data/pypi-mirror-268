import os
import random
import string
from typing import List
from urllib.parse import urlparse
from uuid import UUID

import html2markdown
import requests
from bs4 import BeautifulSoup


class ArticleImporterError(RuntimeError):
    pass


def upload_item_attachment(item_id: int, attachment_uri: str, name=None):
    """Uploads an attachment of an item to the workbench database.

    :param item_id:
    :param attachment_uri: uri of the attachment you're trying to upload.
    :param name: name of the attachment, defaults to None.
    """
    suffix = urlparse(attachment_uri).path.split(".")[-1]
    resp = requests.get(attachment_uri, stream=True)
    file_name = (
        name
        if name
        else f"{''.join(random.choices(string.ascii_uppercase + string.digits, k=8))}.{suffix}"
    )
    file_path = os.path.join(request.folder, "uploads", file_name)

    with open(file_path, "wb") as f:
        # write the file with binary contents of the response object.
        f.write(resp.content)
        with open(file_path, "rb") as f:
            # we're opening the file handle again, this time in read-binary mode.
            # else the actual file will have no contents when uploaded.
            workbench_db.source_file.validate_and_insert(
                item_id=item_id,
                name=file_name,
                original_uri=attachment_uri,
                attachment=f,
            )
    # deleting the file, as this is only meant to be temporary. we don't need it anymore,
    # since the file will be uploaded as an attachment.
    os.unlink(file_path)


def generic_importer(
    contact_id: int = None,
    title: str = None,
    raw: str = None,
    ori_uri: str = None,
    attachments: list = None,
    tag_gids: List[UUID] = None,
    comment: str = None,
    property_bag: dict = None,
):
    """Generic import function.

    :param contact_id: contact_id, defaults to None.
    :param title: title of the article to be imported.
    :param raw: raw text of the article to be imported.
    :param ori_uri: original uri of the article to be imported.
    :param attachments: attachments belonging to the article to be imported.
    :param tag_gids: list of tag_gids that belong to the article to be imported.
    :param comment: comment to be added to the new item.
    :param property_bag: property bag belonging to the item.
    :return: id of the newly created item.
    """
    new_draft_item = workbench_db.item.validate_and_insert(
        contact_id=contact_id,
        title=title,
        ori_uri=ori_uri,
        raw_text=raw,
        raw_frozen=True,
        property_bag=property_bag,
    )
    for tag_gid in tag_gids or []:
        workbench_db.item_tag.validate_and_insert(
            item_id=new_draft_item.id, tag_gid=str(tag_gid)
        )

    for attachment in attachments or []:
        if isinstance(attachment, str):
            upload_item_attachment(item_id=new_draft_item.id, attachment_uri=attachment)

        elif isinstance(attachment, dict):
            # in this case the attachments are coming from the GraphQL backend
            upload_item_attachment(
                item_id=new_draft_item.id,
                attachment_uri=attachment["uri"],
                name=attachment["filename"],
            )

    add_comment(
        tablename="item",
        record_id=new_draft_item.id,
        body=f"""ori_uri: {ori_uri} \n
                {comment if comment else []}""",
    )

    return new_draft_item.id


def delen_met_eddie_importer(url) -> int:
    """Imports item from delen.meteddie.nl

    :arg url: delen.meteddie.nl url
    :returns: the new item.id
    """
    # url is always in the http://delen.meteddie.nl/item/gid?q=vraagtekens format
    gid = urlparse(url).path.split("/")[2]
    item = backend.item(id=gid)
    if not item:
        raise ArticleImporterError("Geen item gevonden met dit URL.")

    raw = html2markdown.convert(item["shortDescription"])
    return generic_importer(
        contact_id=None,
        title=item["name"],
        raw=raw,
        ori_uri=url,
        attachments=item["attachments"],
        tag_gids=[_["id"] for _ in item["tags"]],
        comment="De Eddie importer is blij om iets van delen.meteddie.nl te importeren.",
    )


def import_article_by_url(url) -> int:
    if url.lower().startswith("https://delen.meteddie.nl/item/"):
        return delen_met_eddie_importer(url)
    else:
        try:
            resp = requests.get(url)
            raw_body = resp.text
            dom = BeautifulSoup(raw_body, features="html.parser")
            titles = dom.find_all("title")
            title = titles[0].text if titles else "Geen titel"
            to_attach = []
            for needle in [".pdf", ".xls", ".doc", ".ppt"]:
                to_attach.extend(
                    _.get("href") for _ in dom.find_all("a") if needle in _.get("href")
                )
            article = html2markdown.convert(dom.find("body").text)
            if len(dom.find_all("article")) == 1:
                article = dom.find("article").text
            elif len(dom.find_all("main")) == 1:
                article = dom.find("main").text
            body_text = html2markdown.convert(article)
            return generic_importer(
                contact_id=None,
                title=title,
                raw=body_text,
                ori_uri=url,
                attachments=to_attach,
                tag_gids=[],
                comment="Met de vriendelijke groeten van uw generieke importeermodule.",
            )
        except ArticleImporterError:
            raise ArticleImporterError("Onbekend of ongeldig URL")
        except requests.exceptions.ConnectionError as e:
            session.flash = f"Onbekend of ongeldig URL. \n {str(e)}"
            return redirect(URL("index"))
