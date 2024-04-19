import contextlib
import enum
import functools
import hashlib
import inspect
import string
import typing
import warnings
from typing import Any, Callable, Iterable
from uuid import UUID

import dill
from attrs import asdict, define
from pydal import DAL
from pydal.objects import Rows
from tabulate import tabulate

from .define_models import define_model

TRACK = "track"

CACHE_KEY = "cache_key"

T = typing.TypeVar("T", bound=typing.Any)


@define
class CachedResult(typing.Generic[T]):
    value: T
    required_gids: Iterable[str]


def todb(value: typing.Any) -> bytes:
    return dill.dumps(value)


def fromdb(value: bytes) -> typing.Any:
    return dill.loads(value)


class KeyFormattingError(KeyError):
    pass


class KeyFormattingWarning(UserWarning):
    pass


class DillableAttrsClass:
    @staticmethod
    def todb(item) -> bytes:
        return dill.dumps(asdict(item))

    @classmethod
    def fromdb(cls, dump):
        return cls(**dill.loads(dump))


def cache_ids_which_this_id_depends_on(db, cache_id):
    return db.executesql(
        """
    with recursive composite as (
     select id, cache_id, depends_on from deps where cache_id = %s
    UNION
     select deps.id, deps.cache_id, deps.depends_on from deps inner join composite on  deps.cache_id = composite.depends_on
    )
    select cache_id from composite
    union
    select depends_on from composite
    """,
        fields=[db.deps.cache_id],
        placeholders=(cache_id,),
    )


def cache_ids_that_depend_on(db: DAL, cache_id: str | int) -> Rows:
    return db.executesql(
        """
    select cache_id, cache.gid from derivatives(%s) inner join cache on cache.id = cache_id
    """,
        fields=[db.deps.cache_id, db.cache.gid],
        placeholders=(cache_id,),
    )


class BlackMagic:
    pass


def Magic(arg=BlackMagic):
    warnings.warn("Magic aangeroepn, dat klopt nie. ")
    if arg is BlackMagic:
        return Magic
    return arg


#
# class Magic:
#     def __init__(self, *args, **kwargs) -> None:
#         pass
#     @classmethod
#     def __str__(self):
#         return "It's a kind of magic... magic..."


class ExpectedSortableEnum(Exception):
    """
    Raised when a set of enums is used in the cache key of a cached method.
    By default, enum.Enum can not be compared with eachother.
    Inherit `ValueSortableEnum` instead to fix this issue.
    """


class ValueSortableEnum(enum.Enum):
    """
    Extends the functionality of enum to allow sorting on value.
    See also: ExpectedSortableEnum
    """

    def __gt__(self, other: enum.Enum):
        return self.value > other.value

    def __lt__(self, other: enum.Enum):
        return self.value < other.value


class Cache:
    db: DAL

    def __init__(self, db: DAL) -> None:
        self.db = db

    def __contains__(self, key: Any) -> bool:
        count: int = self.db(self.db.cache.key == str(key)).count()
        return count > 0

    def tracked_setdefault(
        self,
        ptrack: Callable,
        key: Callable,
        generator: Callable,
        todb: Callable = todb,
        fromdb: Callable = fromdb,
    ):
        "if key in cache return value else calculate using generator() and save in cache."

        # blob = self.db.cache(gid=key)
        # if blob is not None:
        #     print(f'Cache hit setdefault({key}, ... )')
        #     return fromdb(blob.value)
        # self.db.cache.insert(gid=key, value=todb(value := generator()))
        # print(f'setdefault saved new {key}')
        # return value
        # y('before tracked_setdefault.decorated',locals())
        @cached(self.db, key, todb=todb, fromdb=fromdb)
        def decorated(track=Magic, cache_key=Magic):
            # y('withing tracked_setdefault.decorated',locals())
            ptrack(cache_key)
            return generator(key, track)

        return decorated()

        # decorated = cached(self.db, key, todb=todb, fromdb=fromdb)(generator)
        # return decorated()


def clean_arguments(args: dict) -> dict:
    """
    Convert sets to ordered lists so the cache key stays consistant
    """
    try:
        return {
            key: sorted(item) if isinstance(item, set) else item
            for key, item in args.items()
        }
    except TypeError as e:
        if "not supported between instances" in str(e):
            raise ExpectedSortableEnum(str(e))


def hash(value: str | bytes):
    """
    Calculate hash value of a (long) string.

    If the value is not a string or bytes, repr() is used and a RuntimeWarning is raised.
    """
    if not isinstance(value, (str, bytes)):
        warnings.warn(
            f"Value {value} is not a string or bytes, repr() is used.",
            category=RuntimeWarning,
        )
        value = repr(value)

    hasher = hashlib.sha1()
    hasher.update(value.encode() if isinstance(value, str) else value)
    return hasher.hexdigest()


P = typing.ParamSpec("P")  # the arguments of the decorated function
R = typing.TypeVar("R")  # the return type of the decorated function

F = typing.TypeVar("F", bound=typing.Callable[P, R])
# bound with typevar should be illegal but mypy and pycharm both seem to prefer it!


def cached(
    db: DAL,
    key: str | Callable,
    todb: Callable[[typing.Any], bytes | str] = lambda x: x,
    fromdb: Callable[[typing.Any], R] = lambda x: x,
    silence_key_warning: bool = False,
    ttl: int | None = None,
) -> typing.Callable[[F], F]:
    """
    Caches the decorated method in postgres, with dependency tracking using the provided `track` keyword argument.

    The cache key can Magically appear similarly using (..., track=Magic, cache_key=Magic).

    /!\ Warning: the transaction is not committed, so in case of an exception, no changes to the cache will be stored.

    Geen thread local variables meer, maar via een nonlocal wordt er een bound functie gemaakt en afgegeven via een
    argument. MITS dat default argument bestaat en een default waarde van Magic heeft.
    Dan is het een bewuste gebruikerskeuze.

    Hierdoor is een return type van CachedResult niet meer nodig (maar wordt nog wel ondersteund mocht die spontaan
    ontstaan, zodat een functie eigen tracking kan toevoegen, buiten de trackers om).
    Typehinting blijft hierdoor beter, de result blijft wat de gebruiker verwacht (een Item ipv CacheResult met een
    .value waar ineens de Item in zit)

    Note: return type should actually be 'typing.Callable[[typing.Callable[P, R]], typing.Callable[P, R]]'
    according to mypy, but that confused PyCharm!
    """
    key_template = key
    # formatter = string.Formatter()

    def cache_wrapper(func: F) -> F:
        # Create a new cached function
        fn_sig = inspect.signature(func)
        fn_parameters = fn_sig.parameters
        fn_has_track_arg = (
            TRACK in fn_parameters and fn_parameters[TRACK].default == Magic
        )
        fn_has_cache_key_arg = (
            CACHE_KEY in fn_parameters and fn_parameters[CACHE_KEY].default == Magic
        )
        if callable(key):
            key_parameters = inspect.signature(key).parameters
            if (
                list(key_parameters.values())[-1].kind != inspect.Parameter.VAR_KEYWORD
                and len(set(key_parameters) - set(fn_parameters)) > 0
            ):
                raise KeyFormattingError(
                    f"Callabe key {key!r} arguments {key_parameters!r} do not match the function's arguments: {fn_parameters!r}"
                )

        else:
            try:
                key.format(**fn_parameters)
            except Exception:
                if not silence_key_warning:
                    warnings.warn(
                        f"\n/!\ /!\ WARNING:\n\tTemplate key {key!r} does not match the function's arguments: {fn_parameters!r}",
                        KeyFormattingWarning,
                        stacklevel=3,
                    )

        @functools.wraps(func)
        def cached_func(*args: P.args, **kwargs: P.kwargs) -> R:
            # y(func, strip_first_arg, inspect.isfunction(func), inspect.ismethod(func))
            # instance methods are not functions
            # if repr(func).startswith('<bound '):
            #     # if it's a method, the "self" or "class" variable will be prepended when calling.
            #     # otherwise all arguments shift one, and keyword and value arguments can collide.
            #     # PITA
            #     args = args[1:]
            # calculate the key based on key_template and values
            function_arguments = fn_sig.bind(*args, **kwargs).arguments
            function_arguments = clean_arguments(function_arguments)

            if callable(key_template):
                # y(func, args, kwargs)
                # y(func, fn_sig.bind(*args, **kwargs).arguments)
                try:
                    key = key_template(**function_arguments)
                except TypeError as e:
                    print(repr(e))
                    breakpoint()
                    raise
            else:
                try:
                    try:
                        key = key_template.format(**function_arguments)
                    except Exception as e:
                        warnings.warn(e)
                        args = list(args)
                        args.pop(0)  # try to remove self and see if that works
                        key = key_template.format(**function_arguments)
                except Exception as e:
                    raise KeyFormattingError(
                        f'Formatting failed for cache key "{key_template}" using {args!r} and {kwargs!r} for fn {func!r} due to {e}'
                    )
            # If entry is cached, return from cache
            # cached = db.cache(gid=key)
            # that was the easy part, let's auto update lr (last read) and increments reads
            cached = db.executesql(
                """
                update cache
                set reads = reads + 1,
                    lr    = current_timestamp
                where gid = %s
                returning id, value, EXTRACT(EPOCH FROM (localtimestamp - ts)) > ttl as expired
            """,
                placeholders=(key,),
                fields=[db.cache.id, db.cache.value, db.cache.expired],
            )

            if cached:
                # cache_id, value, expired = cached[0]
                cached = cached.first()
                cache_id, value, expired = cached.id, cached.value, cached.expired
                # expired can be True, False or None.
                # True is expird, False is still active, None is no TTL set.
                print(f'Cache hit "{key}", {expired}, {len(value)},', hash(value))
                if expired in (False, None):
                    # print(f'Cache hit "{key}", {expired}, {len(value)}')
                    return fromdb(value)
                elif expired is True:
                    # delete the key
                    db(db.cache.gid == key).delete()
                    # delete all that depend on this key
                    remove_these_cached_gids_that = {
                        row.deps.cache_id
                        for row in cache_ids_that_depend_on(db, cache_id)
                    }
                    print(
                        "Cache expired, killed row and will kill",
                        len(remove_these_cached_gids_that),
                        "derivatives.",
                    )
                    db(db.cache.id.belongs(remove_these_cached_gids_that)).delete()
                    db.commit()
            # create a new set per function,
            tracked_gids = set()

            if fn_has_track_arg:
                # create a new tracker method per function call, bound to this above set
                # to avoid reentrency problems
                def track(
                    references: CachedResult[R] | UUID | list[UUID] | str | list[str],
                ):
                    """Returns cachedresult.value but keeps track of the required_gids."""
                    nonlocal tracked_gids
                    if isinstance(references, CachedResult):
                        tracked_gids |= set(references.required_gids)
                        return references.value
                    elif isinstance(references, UUID):
                        tracked_gids |= {str(references)}
                    elif isinstance(references, str):
                        tracked_gids |= {references}
                    elif isinstance(references, list):
                        tracked_gids |= {str(ref) for ref in references}
                    else:
                        raise ValueError(f"Unknown trackable type: {references!r}")
                    # print('Track called:',repr(references), 'total: ',tracked_gids )
                    return references

                # call any existing passed tracker to
                # track the current key id
                if TRACK in kwargs:
                    kwargs[TRACK](key)

                # add the tracker to the arguments
                kwargs[TRACK] = track
            else:
                print("CACHE WARNING:", key, "requires no track arguments")
            if fn_has_cache_key_arg:
                # if the function expects the cache_key, insert it here
                kwargs[CACHE_KEY] = key

            # If not cached, execute , add to cache and return value
            # execute
            print("Execute", key)
            # this makes sure returned.value -> R
            returned = typing.cast(
                CachedResult[R], func(*args, **kwargs)
            )  # either it is a cached result or it is converted later.

            # book requirements
            if isinstance(returned, CachedResult):
                # assume there is a list of gids to keep an eye on
                tracked_gids |= set(returned.required_gids)
            else:
                # assume no list of items was specifically returned, just use the tracked once,
                # which are already in tracked_gids
                # raise ValueError(f'Cached function {func} did not return a CachedResult, but {returned!r} instead.')
                returned = CachedResult(returned, tracked_gids)
            # insert to cache
            # print(f'Save to stash "{key}", "{returned.value!r}" requires {returned.required_gids!r}')
            str_value = todb(returned.value)
            print(
                f'Cached decorator, SAVE "{key}"',
                hash(str_value),
                # returned.required_gids,
            )
            cache_id = db.cache.insert(gid=key, value=str_value, ttl=ttl)
            # keep unique
            tracked_gids = set(tracked_gids)
            if tracked_gids:
                # fixen dat gids die niet voorkomen in de cache tabel via een fake record in de cache komen.
                # dan zijn ze in ieder geval te gebruiken als selectie van dependencies.
                gids_seen_in_cache = {
                    rec.gid
                    for rec in db(db.cache.gid.belongs(tracked_gids)).select(
                        db.cache.gid
                    )
                }
                missing_gids = tracked_gids - gids_seen_in_cache
                db.cache.bulk_insert(
                    (dict(gid=gid, value="Externally defined.") for gid in missing_gids)
                )
                # nu zou alles er moeten zijn.
                sub_select = db(db.cache.gid.belongs(tracked_gids))._select(
                    cache_id, db.cache.id
                )
                db.executesql(
                    """
                    insert into deps (cache_id, depends_on)
                """
                    + sub_select
                )
            # after having registered all the dependencies, return with the current key as the new dependency
            return returned.value

        # Return our new cached function
        return typing.cast(
            F, cached_func
        )  # just return the function but make mypy happy

    return cache_wrapper


def clear_cache(db: DAL, gid_needle: str) -> None:
    # not using db.cache because it may not be defined yet
    # so using executesql directly we avoid the error of the table not existing yet
    # as well as having to define the table in the model
    print(f"clearing cache for {gid_needle!r}")
    db.executesql(
        """
        delete from cache where gid like %s;
    """,
        placeholders=(gid_needle,),
    )
    db.commit()


def cache_hook_table_with_gid(db, table_rname):
    # db.executesql('listen cacheinvalidation')
    # db.rollback()
    db.executesql(
        f"""
    CREATE OR REPLACE FUNCTION cache_{table_rname}_update() RETURNS trigger AS $cache_{table_rname}_update$
        declare
            cache_id int;
        BEGIN
            select id into cache_id from cache where cache.gid = NEW.gid;
            delete from cache using derivatives(cache_id) dep where cache.id = dep.cache_id;
            -- perform pg_notify('cacheinvalidation', NEW.gid::text);
            RETURN NEW;
        END;
    $cache_{table_rname}_update$ LANGUAGE plpgsql;
    """
    )
    db.executesql(
        f"""
    create or replace TRIGGER cache_{table_rname}_update_trigger AFTER UPDATE ON item
        FOR EACH ROW EXECUTE FUNCTION cache_{table_rname}_update();
    """
    )
    db.commit()


def debug_cache_dependencies(db):
    return tabulate(
        db.executesql(
            """
            select cache.gid, dep.gid 
              from deps 
                inner join cache on cache.id = deps.cache_id 
                inner join cache dep on dep.id = deps.depends_on
            """
        ),
        headers=["cache_id", "depends_on"],
    )


def show_rows(title=None, rows=None, tablefmt="github"):
    if rows is None:
        rows, title = title, rows
    if not isinstance(rows, list):
        rowlist = rows.as_list()
    else:
        rowlist = rows
    table = tabulate(rowlist, headers="keys", tablefmt=tablefmt)
    if title:
        width = len(table.split("\n")[0])
        dashes = width - len(title) - 4
        c1 = dashes // 2
        c2 = dashes - c1
        print(f'{"-" * c1}[ {title} ]{"-" * c2}')
    print(table)
    print()
