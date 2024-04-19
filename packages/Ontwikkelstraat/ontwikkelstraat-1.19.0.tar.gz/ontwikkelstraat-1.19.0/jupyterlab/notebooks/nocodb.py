from abc import ABC
from dataclasses import dataclass
from pprint import pprint
from urllib.parse import urlencode

import requests

META_TMPL = "{base}/meta"
DATA_TMPL = "{base}/data/noco/{project}"


class NocoApi(ABC):
    _headers: dict

    _base_data_url: str
    _base_meta_url: str

    _meta = False
    session = requests.Session()

    def __create_url(self, *paths, query_dict=None, _meta=False):
        parts = [
            self._base_meta_url if (self._meta or _meta) else self._base_data_url,
            *paths,
        ]
        url = "/".join([str(p) for p in parts if p])

        if query_dict:
            url += "?" + urlencode(query_dict)

        return url

    def _get(self, *action, query_dict=None, _meta=False, _full_url=None):
        if query_dict is None:
            query_dict = {}

        if isinstance(query_dict.get("where"), tuple):
            query_dict["where"] = f'({",".join(query_dict["where"])})'

        if _full_url is None:
            url = self.__create_url(*action, query_dict=query_dict, _meta=_meta)
        else:
            url = _full_url
        return self.session.get(url, headers=self._headers).json()

    def _post(self, *action, data=None):
        if data is None:
            data = {}

        url = self.__create_url(*action)

        return self.session.post(url, json=data, headers=self._headers).json()

    def _patch(self, *action, data=None):
        if data is None:
            data = {}

        url = self.__create_url(*action)

        return self.session.patch(url, json=data, headers=self._headers).json()

    def _delete(self, *action):
        url = self.__create_url(*action)

        return self.session.delete(url, headers=self._headers).json()


@dataclass
class NocoClient(NocoApi):
    _domain: str
    _project: str
    _api_key: str

    _headers = {}

    def __post_init__(self):
        self._headers["xc-token"] = self._api_key
        self._api_base = f"{self._domain}/api/v1/db"

        # note: _project = external/data, _project_id = internal/meta
        self._project_id = self.__convert_project_name_to_id(self._project)
        self._base_data_url = DATA_TMPL.format(
            base=self._api_base, project=self._project
        )

        self._base_meta_url = META_TMPL.format(base=self._api_base)
        self.meta_ = NocoMeta(self)  # <- requires _project_id
        self.tables_ = [t["title"] for t in self.meta_.table_list()]

    def _project_list(self, _full=True):
        # special route because 'meta' does not exist yet

        # todo: support page, pageSize, sort
        projs = self._get(
            "projects", query_dict={}, _full_url=f"{self._api_base}/meta/projects/"
        ).get("list", [])
        if _full:
            return projs
        return {p["title"]: p["id"] for p in projs}

    def __convert_project_name_to_id(self, human_name):
        names = self._project_list(_full=False)

        if names.get(human_name):
            return names.get(human_name)
        else:
            raise ValueError(f"Project '{human_name}' could not be found.")

    def __getattr__(self, item):
        if item.startswith("_"):
            return super().__getattribute__(item)

        if item not in self.tables_:
            raise ValueError(f"Table '{item}' could not be found.")

        return NocoTable(item, self)

    # todo: support other meta CRUD operations

    def __dir__(self):
        og = [f for f in super().__dir__() if not f.startswith("_")]
        return [*self.tables_, *og]


@dataclass
class NocoMeta(NocoApi):
    client: NocoClient

    def __post_init__(self):
        self._base_meta_url = self.client._base_meta_url
        self._headers = self.client._headers
        self._meta = True

        self._tables = {t["title"]: t["id"] for t in self.table_list()}

    def project_list(self, _full=True):
        return self.client._project_list(_full)

    def table_list(self):
        # todo: page, pagesize, sort, includem2m
        return self._get(
            "projects", self.client._project_id, "tables", query_dict={}
        ).get("list", [])

    def convert_table_name_to_id(self, name):
        id = self._tables.get(name)
        if not id:
            raise ValueError(f"Table '{name}' could not be found.")
        return id

    def table_read(self, id, _raw=False):
        if not _raw:
            id = self.convert_table_name_to_id(id)
        return self._get("tables", id)


@dataclass
class NocoTable(NocoApi):
    name: str
    client: NocoClient

    def __post_init__(self):
        self.__previous__ = None
        self.__history__ = []

        self._headers = self.client._headers
        self._base_data_url = self.client._base_data_url + "/" + self.name

    # R

    def list(self, query_dict):
        return self._get("", query_dict=query_dict)

    def count(self, query_dict):
        return self._get("count", query_dict=query_dict)

    def read(self, id, query_dict):
        return self._get(id, query_dict=query_dict)

    def __getitem__(self, x):
        # noco.table[id] is an alias of noco.table.read(id)
        if isinstance(x, tuple):
            id, query = x
        else:
            id = x
            query = {}

        # we ondersteunen query maar read ondersteunt verder geen opties:
        # https://all-apis.nocodb.com/#operation/db-table-row-update
        return self.read(id, query)

    # C
    def create(self, data):
        return self._post(data=data)

    def __add__(self, data):
        # noco.table += {} is an alias for noco.table.create({})
        self.__previous__ = self.create(data)
        self.__history__.append(("add", self.__previous__))
        return self

    # U
    def update(self, id, data):
        return self._patch(id, data=data)

    def __setitem__(self, id, data):
        self.__previous__ = self.update(id, data)
        self.__history__.append(("update", self.__previous__))
        return self

    # D
    def delete(self, id):
        return self._delete(id)

    def __sub__(self, id):
        self.__previous__ = self.delete(id)
        self.__history__.append(("delete", self.__previous__))
        return self

    # many to many / m2m
    def m2m(self, this_id, this_col, that_id):
        # {table}/{id}/mm/{col}/{foreign_id}
        return self._post(this_id, "mm", this_col, that_id).get("msg", "")

    def delete_m2m(self, this_id, this_col, that_id):
        # {table}/{id}/mm/{col}/{foreign_id}
        return self._delete(this_id, "mm", this_col, that_id).get("msg", "")

    # hasmany / hm
    def hm(self, this_id, this_col, that_id):
        # {table}}/{this_id}/hm/{this_col}/{that_id}
        return self._post(this_id, "hm", this_col, that_id).get("msg", "")

    def delete_hm(self, this_id, this_col, that_id):
        return self._delete(this_id, "hm", this_col, that_id).get("msg", "")
