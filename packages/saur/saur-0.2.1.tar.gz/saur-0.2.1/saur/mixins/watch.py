from __future__ import annotations
from collections import defaultdict
from typing import AsyncIterator, Callable, TypeVar, Generic
from asyncio import sleep, Event
from weakref import WeakValueDictionary
from datetime import datetime, timedelta, UTC
from typing import TYPE_CHECKING

from sqlalchemy import inspect, and_
from sqlalchemy.sql.expression import select

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

__all__ = ["Watcher"]

T = TypeVar("T")


class Watchable(Generic[T]):
    def __init__(self, data: T | None = None):
        self._data = data
        self.event = Event()

    @property
    def data(self) -> T:
        return self._data

    @data.setter
    def data(self, value: T) -> None:
        self._data = value
        self.event.set()
        self.event = Event()

    async def __aiter__(self) -> AsyncIterator[T]:
        last_sent = None
        while self._data is None:
            await sleep(0.1)
        while True:
            event = self.event
            data = self.data
            if data != last_sent:
                yield data
                last_sent = data
            await event.wait()

    async def __call__(self, post_processor: Callable | None=None):
        async for value in self:
            if post_processor is None:
                yield value
            else:
                yield post_processor(value)

class WatchedModel:
    def __init__(self, model, updated_column):
        self.model = model
        self.primary_key_fields = {field.name: field for field in inspect(model).primary_key}
        self.primary_key_field_names = sorted(self.primary_key_fields.keys())
        if isinstance(updated_column, str):
            updated_column = getattr(model, updated_column)
        self.updated_column = updated_column
        self.registry = WeakValueDictionary()
        self.last_checked = None

    def watch(self, selector: dict, post_processor: Callable | None = None) -> AsyncIterator:
        if sorted(selector.keys()) != self.primary_key_field_names:
            msg = "Selector must include exactly the model primary keys."
            raise ValueError(msg)
        selector_values = tuple(selector[k] for k in self.primary_key_field_names)
        obj = self.registry.get(selector_values)
        if obj is None:
            obj = Watchable()
            self.registry[selector_values] = obj
        return obj(post_processor)

    def watch_obj(self, obj, post_processor: Callable | None = None) -> AsyncIterator:
        selector = {k: getattr(obj, k) for k in self.primary_key_field_names}
        return self.watch(selector, post_processor)

    async def check(self, session: AsyncSession, backoff: float):
        if not self.registry:
            return
        now = datetime.now(UTC)
        now_backoff = now - timedelta(seconds=backoff)
        pk_values = defaultdict(set)
        for selector in self.registry:
            for key, value in zip(self.primary_key_field_names, selector):
                pk_values[key].add(value)
        filters = [
            pk_field.in_(pk_values[pk_name])
            for pk_name, pk_field in self.primary_key_fields.items()
        ]
        if self.last_checked is not None:
            filters.append(self.updated_column >= self.last_checked)
        query = select(self.model).filter(and_(*filters))
        updated = []
        for result in await session.scalars(query):
            selector = tuple(getattr(result, key) for key in self.primary_key_field_names)
            obj = self.registry.get(selector)
            if obj is not None:
                obj.data = result
            updated.append(getattr(obj, self.updated_column.name))
        # ?!?! backoff for update & checking ... ???
        if updated:
            self.last_checked = min(now_backoff, max(updated))
        else:
            self.last_checked = now_backoff


class Watcher:
    def __init__(self, session: AsyncSession, polling_period: float = 2.0, backoff: float = 10.0):
        self.session = session
        self.models = {}  # of WeakValueDictionary
        self.polling_period = polling_period
        self.backoff = backoff

    def register_watched_model(self, model, updated_column) -> WatchedModel:
        if isinstance(updated_column, str):
            updated_column = getattr(model, updated_column)
        if watched_model := self.models.get(model):
            if watched_model.updated_column != updated_column:
                msg = "Cannot changed updated column"
                raise ValueError(msg)
            return watched_model
        watched_model = WatchedModel(model, updated_column)
        self.models[model] = watched_model
        return watched_model

    def watch(self, model, selector: dict, post_processor: Callable | None = None) -> AsyncIterator:
        return self.models[model].watch(selector, post_processor)

    def watch_obj(self, obj, post_processor: Callable | None = None) -> AsyncIterator:
        model = type(obj)
        return self.models[model].watch_obj(obj, post_processor)

    async def run(self) -> None:
        while True:
            for watched_model in self.models.values():
                await watched_model.check(self.session, self.backoff)
            await sleep(self.polling_period)


# usage
# watcher = Watcher(session)
# async for version in watcher.watch(Model, {"id": 1},
#   partial(PydanticModel.validate_model, from_attributes=True)):
#    send(version)
