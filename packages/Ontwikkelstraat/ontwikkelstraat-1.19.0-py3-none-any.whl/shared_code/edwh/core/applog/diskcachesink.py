import json
from datetime import datetime
from functools import singledispatch
from uuid import UUID

## copy from edwh.backend.engine
from attrs import asdict
from celery import Task
from diskcache import Deque

from .sink import SignalSink


## copy from edwh.core.backend.engine
def serialize_backend_types(instance, field, value):
    """
    Used for attrs.asdict magic.

    See https://www.attrs.org/en/stable/api.html#attr.asdict :

    value_serializer (Optional[callable]) – A hook that is called for every attribute or
    dict key/value. It receives the current instance, field and value and must return the
    (updated) value. The hook is run after the optional filter has been applied.

    web2py example:

    def demo():
        from attrs import asdict

        # return response.json(asdict(backend.pratices(search=request.vars.q)))
        return response.json(
            asdict(
                backend.pratices(search=request.vars.q),
                value_serializer=serialize_backend_types,
            )
        )

    """
    if isinstance(value, UUID):
        return str(value)
    elif isinstance(value, bytes):
        return value.decode()
    return value


def filter_backend_types(attr, value):
    return not attr.name.startswith("_")


def edwh_asdict(instance):
    return asdict(
        instance,
        value_serializer=serialize_backend_types,
        filter=filter_backend_types,
    )


### /copy


### Json converters
@singledispatch
def to_serializable(val):
    """Used by default."""
    try:
        return edwh_asdict(val)
    except:
        return str(val)


@to_serializable.register
def ts_datetime(val: datetime):
    """Used if *val* is an instance of datetime."""
    return val.isoformat()


@to_serializable.register
def ts_bytes(val: bytes):
    """Used if *val* is an instance of datetime."""
    return val.decode("utf-8")


### /json converters


class DequeSink(SignalSink):
    def __init__(
        self,
        task: Task,
        app_id: str,
        app_key: str,
        autocommit: bool = True,
    ):
        super().__init__()
        self.buffer: list[dict] = []
        self.task: Task = task
        self.app_id: str = app_id
        self.app_key: str = app_key
        self.autocommit: bool = autocommit
        self.deque = Deque(directory="/shared_applog")

    def signal(
        self,
        name,
        signal_source,
        evidence=None,
        session_gid=None,
        user_gid=None,
        ts=None,
        related=None,
    ):
        details = locals().copy()
        del details["self"]
        self.buffer.append(details)
        if self.autocommit:
            self.commit()

    def commit(self):
        try:
            # print('sink.commit1 ', self.buffer)
            if not self.buffer:
                return
            # copy from the buffer so additions to the buffer while sending
            # are not reverted by resetting self.buffer to []
            local_buffer = []
            while self.buffer:
                local_buffer.append(self.buffer.pop())
            if len(local_buffer) == 1:
                # with just one, send it straight away
                local_buffer = local_buffer[0]

            # convert to json, to_serializable handles different argument types
            # pprint.pprint(local_buffer)
            data = json.dumps(local_buffer, default=to_serializable)
            # print('sink.commit3', local_buffer)
            with self.deque.transact():
                self.deque.append(data)

            # print('sink.commit4', _)

            return True
        except Exception as e:
            print("ERROR IN COMMIT", e)
            import pprint

            pprint.pprint(local_buffer)
            raise
