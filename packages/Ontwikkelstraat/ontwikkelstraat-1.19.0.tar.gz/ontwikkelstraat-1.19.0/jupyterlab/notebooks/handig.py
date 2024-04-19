# demonstratie doeleinden
zeer_handig = True

from edwh.core.tags import *
from IPython.display import Markdown, display


def human_readable_list_of_tagged_with(Tag, base_tag):
    for filter in base_tag.tagged_with():
        display(Markdown(f"## {filter.name}"))
        for child in filter.children():
            # print(child.name, ':',child.add_metatag(is_user_selectable))
            display(
                Markdown(
                    " * "
                    + child.name
                    + ' <font color="darkgrey">[ '
                    + ", ".join(names([Tag(_) for _ in child.row.meta_tags]))
                    + " ]</font>"
                )
            )
