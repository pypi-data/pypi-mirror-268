import random
import typing
import uuid

from attr import asdict, define, field

if typing.TYPE_CHECKING:
    import json

    from gluon import response

    from ..models.aaa_500_checkbox_widget import width_first_tree_sort
    from ..models.db import auth

tags_by_name: dict[str, "Tag"] = dict()
tags_by_gid: dict[str, "Tag"] = dict()


@define()
class Tag:
    name: str
    gid: str = field(factory=lambda: str(uuid.uuid4()))
    parents: list = field(factory=list)
    children: list = field(factory=list)

    def __attrs_post_init__(self):
        tags_by_name[self.name] = self
        tags_by_gid[self.gid] = self
        self.parents = [tags_by_name.get(str(_), _).gid for _ in self.parents]
        for parent in self.parents:
            _parent = tags_by_gid[parent]
            if self.gid not in _parent.children:
                _parent.children.append(self.gid)
        self.children = [tags_by_name.get(str(_), _).gid for _ in self.children]
        for child in self.children:
            _child = tags_by_gid[child]
            if self.gid not in _child.parents:
                _child.parents.append(self.gid)


# /scratch/boom
@auth.requires_login()
def boom():
    Tag("root"),
    Tag("A1", parents=["root"], children=[Tag("A1,A2.1"), Tag("A1.2"), Tag("A1.3")])
    Tag("A2", parents=["root", "A1"], children=["A1,A2.1", Tag("A2.1")])
    Tag("B1", parents=["A2.1"])
    Tag("circular", parents=["B1"])

    tags_by_name["B1"].parents.append("circular")
    # tags_by_name['A2'].parents.append('onbekend')
    flat_data = list(tags_by_name.values())

    random.shuffle(flat_data)

    # # ---- hierboven nietmeer aankomen.
    # dest = {}
    # source = flat_data[:]
    # last_diff = -1
    # while diff := len(source) - len(dest):
    #     for tag in source:
    #         if tag.gid in dest:
    #             # tag is behandeld
    #             continue
    #         if any(parent not in dest for parent in tag.parents):
    #             # not niet elke parent is gezien, dus deze negeren
    #             continue
    #         dest[tag.gid] = tag
    #     if last_diff == diff:
    #         raise HTTP(508, 'Infinite Loop Detected')
    #     last_diff = diff

    # ---- hierboven nietmeer aankomen.
    tree_data = width_first_tree_sort(flat_data)

    response.headers["Content-Type"] = "application/json"
    return json.dumps(tree_data, default=asdict, indent=2)


# def width_first_tree_sort(tag_list):
#     dest = {}
#     source = tag_list[:]
#     last_diff = -1
#     loop_count = 0
#     while source:
#         loop_count += 1
#         diff = len(source)
#         source_index = 0
#         for tag in source.copy():
#             if any(parent not in dest for parent in tag.parents):
#                 # not niet elke parent is gezien, dus deze negeren
#                 source_index += 1
#                 continue
#             else:
#                 dest[tag.gid] = tag
#                 del source[source_index]
#
#         if last_diff == diff:
#             raise HTTP(508, 'Infinite Loop Detected')
#         last_diff = diff
#     return dest
