import enum
import json
import os
from functools import partial

import httpx
from attrs import asdict, define, field

NTFY_ERROR_URL = os.getenv("NTFY_ERROR_URL")
NTFY_WARNING_URL = os.getenv("NTFY_WARNING_URL")
NTFY_SORT_URL = os.getenv("NTFY_SORT_URL")


class Priority(enum.Enum):
    MAX = 5
    URGENT = 5
    HIGH = 4
    DEFAULT = 3
    LOW = 2
    MIN = 1


class Action:
    ...


@define
class View(Action):
    #  see https://ntfy.sh/docs/publish/#open-websiteapp
    url: str
    label: str | None
    clear: bool


@define
class Click(Action):
    url: str
    lable: str | None


@define
class Http(Action):
    ...
    # see https://ntfy.sh/docs/publish/#send-http-request


@define
class Attachment(Action):
    ...
    # see https://ntfy.sh/docs/publish/#attachments


def notify(
    url: str,
    message: str,
    title: str = None,
    priority: Priority | None = None,
    tags: list[str] = None,
    click_url: str | None = None,
    actions: list[Action] | None = None,
    icon: str | None = None,
) -> None:
    # for tags see: https://ntfy.sh/docs/publish/#tags-emojis
    data = dict(message=message)
    if title:
        data["title"] = title
    if priority:
        data["priority"] = priority.value
    if tags:
        data["tags"] = [str(_).strip().lower() for _ in tags]
    if click_url:
        data["click"] = click_url
    if actions:
        data["actions"] = []
        for action in actions:
            action_dict = {"action": action.__class__.__name__}
            for k, v in asdict(action).items():
                if v:
                    action_dict[k] = getattr(action, k)
            data["actions"].append(action_dict)
    if icon:
        data["icon"] = icon
    url, data["topic"] = url.rsplit("/", 1)
    print(json.dumps(data, indent=4))
    return httpx.post(url, data=json.dumps(data))


def error(
    message: str,
    title: str = None,
    priority: Priority | None = None,
    tags: list[str] = None,
    click_url: str | None = None,
    actions: list[Action] | None = None,
    icon: str | None = None,
) -> None:
    return notify(
        NTFY_ERROR_URL, message, title, priority, tags, click_url, actions, icon
    )


def warning(
    message: str,
    title: str = None,
    priority: Priority | None = None,
    tags: list[str] = None,
    click_url: str | None = None,
    actions: list[Action] | None = None,
    icon: str | None = None,
) -> None:
    return notify(
        NTFY_WARNING_URL, message, title, priority, tags, click_url, actions, icon
    )


def onbekend(
    message: str,
    title: str = None,
    priority: Priority | None = None,
    tags: list[str] = None,
    click_url: str | None = None,
    actions: list[Action] | None = None,
    icon: str | None = None,
) -> None:
    return notify(
        NTFY_SORT_URL, message, title, priority, tags, click_url, actions, icon
    )
