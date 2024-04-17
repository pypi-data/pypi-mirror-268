from __future__ import annotations
from typing import Self, Any, Collection, TYPE_CHECKING
from asyncio import gather

# from functools import cached_property
from inspect import getmembers_static

from sqlalchemy import inspect, Column, update
from sqlalchemy.orm import selectinload, QueryableAttribute, declarative_mixin
from sqlalchemy.sql.expression import select, Select, delete, and_
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.hybrid import hybrid_property
from cytoolz import keyfilter  # pylint:disable=no-name-in-module

__all__ = ["AsyncAccessMixin"]

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession
    from sqlalchemy.engine import ScalarResult
    from sqlalchemy.sql.expression import ColumnElement, Delete


def is_property(obj: Any) -> bool:
    return isinstance(obj, (property, hybrid_property))


SelectFieldType = QueryableAttribute | Collection[QueryableAttribute]


def select_fields(
    query: Select,
    fields: Collection[SelectFieldType],
) -> Select:
    if not fields:
        return query
    options = []
    for field in fields:
        if isinstance(field, QueryableAttribute):
            option = selectinload(field)
        elif not field:
            continue
        else:
            option = selectinload(field[0])
            for step in field[1:]:
                option = option.selectinload(step)
        options.append(option)
    return query.options(*options)


@declarative_mixin
class AsyncAccessMixin:
    # later: auto-rewrite all varkwargs signatures with model fields

    # @cachedproperty desired, but error:
    # `Cannot use cached_property instance without calling __set_name__ on it.`
    @classmethod
    @property
    def _primary_keys(cls) -> tuple[Column, ...]:
        return inspect(cls).primary_key

    # @cachedproperty desired, but error:
    # `Cannot use cached_property instance without calling __set_name__ on it.`
    @classmethod
    @property
    def _field_names(cls) -> set[str]:
        orm_props = {prop.key for prop in inspect(cls).iterate_properties}
        py_props = {
            name for (name, _) in getmembers_static(cls, is_property) if not name.startswith("_")
        }
        return orm_props | py_props

    def to_dict(self, fields: Collection[str] | None = None) -> dict[str, Any]:
        if fields is None:
            return keyfilter(self._field_names.__contains__, self.__dict__)
        return {k: getattr(self, k) for k in fields}

    # basic queries

    @classmethod
    def select(
        cls,
        *with_fields: SelectFieldType,
        **filters,
    ) -> Select:
        # with_fields as QueryableAttribute or list/tuple[QueryableAttribute]
        #  - in latter: selectinload chain
        query = select_fields(select(cls), with_fields)
        if filters:
            query = query.filter_by(**filters)
        return query

    @classmethod
    def select_pk(
        cls,
        primary_key: Any,
        /,
        *with_fields: SelectFieldType,
        **filters,
    ) -> Select:
        try:
            (pk_field,) = cls._primary_keys
        except TypeError as exc:
            msg = "Can only use pk shorthand for single-pk models"
            raise TypeError(msg) from exc
        filters[pk_field.name] = primary_key
        return cls.select(*with_fields, **filters)

    @classmethod
    def where(cls, **filters) -> ColumnElement:
        collect = []
        for key, value in filters.items():
            attr = getattr(cls, key)
            collect.append(attr == value)
        return and_(*collect)

    # basic get

    @classmethod
    async def find(
        cls,
        *with_fields: SelectFieldType,
        session: AsyncSession,
        **filters,
    ) -> ScalarResult[Self]:
        query = cls.select(*with_fields, **filters)
        return await session.scalars(query)

    @classmethod
    async def find_one(
        cls,
        *with_fields: SelectFieldType,
        session: AsyncSession,
        **filters,
    ) -> Self:
        query = cls.select(*with_fields, **filters)
        result = await session.execute(query)
        return result.scalar_one()

    @classmethod
    async def get(
        cls,
        primary_key: Any,
        /,
        *with_fields: SelectFieldType,
        session: AsyncSession,
        **filters,
    ) -> Self:
        query = cls.select_pk(primary_key, *with_fields, **filters)
        result = await session.execute(query)
        return result.scalar_one()

    async def with_fields(
        self,
        *with_fields: str | Collection[str],
        session: AsyncSession,
        force: bool = False,
    ) -> Self:
        # !! TODO: nested with fields
        unloaded = inspect(self).unloaded
        if (set(with_fields) & set(unloaded)) or force:
            await session.refresh(self, attribute_names=with_fields)
        return self

    # create - update - delete (& upsert)

    @classmethod
    async def create(
        cls,
        *,
        session: AsyncSession,
        commit: bool = True,
        refresh: bool = True,
        **kwargs,
    ) -> Self:
        new_obj = cls(**kwargs)
        session.add(new_obj)
        if commit:
            await session.commit()
            if refresh:
                await session.refresh(new_obj)
        return new_obj

    @classmethod
    async def create_if_not_exists(cls, *, session: AsyncSession, **kwargs) -> Self:
        existing = await cls.find(session=session, **kwargs)
        try:
            return existing.one()
        except NoResultFound:
            new_obj = cls.create(session=session, **kwargs)
            await session.commit()
            await session.refresh(new_obj)
            return new_obj

    # pylint:disable=invalid-name
    @classmethod
    async def upsert(
        cls,
        data: dict[str, Any],
        on: Collection[str],
        create_fields: Collection[str] | None = None,
        update_fields: Collection[str] | None = None,
        *,
        session: AsyncSession,
        commit: bool = True,
        refresh: bool = True,
    ) -> Self:
        # later: single statement upsert
        # https://docs.sqlalchemy.org/en/20/orm/queryguide/dml.html#orm-enabled-insert-update-and-delete-statements
        if create_fields is None:
            create_fields = on
        if update_fields is None:
            update_fields = set(data.keys()) - set(on)
        on_data = keyfilter(on.__contains__, data)
        existing_results = await cls.find(session=session, **on_data)
        try:
            obj = existing_results.one()
        except NoResultFound:
            create_data = keyfilter(create_fields.__contains__, data)
            obj = await cls.create(session=session, commit=commit, refresh=refresh, **create_data)
        if update_fields:
            update_data = keyfilter(update_fields.__contains__, data)
            await obj.update(session=session, commit=commit, refresh=refresh, **update_data)
        return obj

    @classmethod
    async def multiupsert(
        cls,
        rows: list[dict[str, Any]],
        on: Collection[str],
        create_fields: Collection[str] | None,
        update_fields: Collection[str] | None,
    ) -> None:
        pass

    async def update(
        self,
        *,
        session: AsyncSession,
        commit: bool = True,
        refresh: bool = True,
        **kwargs,
    ) -> Self:
        for key, value in kwargs.items():
            if key not in self._field_names:
                msg = f"Field {key} not settable."
                raise AttributeError(msg)
            setattr(self, key, value)
        session.add(self)
        if commit:
            await session.commit()
            if refresh:
                await session.refresh(self)
        return self

    async def delete(self, *, session: AsyncSession, commit: bool = True) -> None:
        await session.delete(self)
        if commit:
            await session.commit()

    # batch crud

    @classmethod
    async def batch_create(
        cls,
        data: Collection[dict[str, Any]],
        *,
        session: AsyncSession,
        commit: bool = True,
        refresh: bool = False,
        **addl_data,
    ) -> list[Self]:
        # included for api consistency
        results = await gather(
            *[cls.create(session=session, commit=False, **datum, **addl_data) for datum in data],
        )
        if commit:
            await session.commit()
            if refresh:
                for result in results:
                    await session.refresh(result)
        return results

    # pylint:disable=invalid-name
    @classmethod
    async def batch_upsert(
        cls,
        data: Collection[dict[str, Any]],
        on: Collection[str],
        *,
        create_fields: Collection[str] | None = None,
        update_fields: Collection[str] | None = None,
        session: AsyncSession,
        commit: bool = True,
        refresh: bool = False,
    ) -> list[Self]:
        with session.no_autoflush:
            results = [
                await cls.upsert(
                    datum,
                    on,
                    session=session,
                    commit=False,
                    create_fields=create_fields,
                    update_fields=update_fields,
                )
                for datum in data
            ]
        if commit:
            await session.commit()
            if refresh:
                for result in results:
                    await session.refresh(result)
        return results

    @classmethod
    async def batch_update(
        cls,
        where: Collection[dict[str, Any]],
        values: Collection[dict[str, Any]],
        *,
        session: AsyncSession,
    ) -> None:
        statement = (
            update(cls)
            .where(and_(*[getattr(cls, k) == v for k, v in where.items()]))
            .values(**values)
        )
        await session.execute(statement)

    @classmethod
    def batch_delete_query(cls, whereclause: ColumnElement = None, **filters) -> Delete:
        query = delete(cls)
        if whereclause is not None:
            query = query.where(whereclause)
        if filters:
            query = query.where(cls.where(**filters))
        return query

    @classmethod
    async def batch_delete(
        cls, whereclause: ColumnElement = None, *, session: AsyncSession, **filters,
    ) -> None:
        query = cls.batch_delete_query(whereclause, **filters)
        await session.execute(query)

    # correlating lists of objects

    @classmethod
    async def _correlate(
        cls,
        objs: list[Self],
        data: list[dict] | list[Self],
        on: Collection[str],
        *,
        update_fields: Collection[str] | None = None,
        session: AsyncSession,
        commit: bool = True,
        refresh: bool = True,
        **addl_data,
    ) -> tuple[list[dict], list[Self], list[Self]]:
        results = []
        to_create = []
        unseen = list(objs)
        for datum in data:
            for obj in unseen:
                if all(getattr(obj, k) == datum.get(k) for k in on):
                    results.append(obj)
                    unseen.remove(obj)
                    if update_fields is None:
                        to_update = (set(datum.keys()) | set(addl_data.keys())) - set(on)
                    else:
                        to_update = update_fields
                    if to_update:
                        obj_update = {}
                        for k in to_update:
                            existing = getattr(obj, k, None)
                            new = datum.get(k) if k in datum else addl_data.get(k)
                            if new != existing:
                                obj_update[k] = new
                        if obj_update:
                            await obj.update(**obj_update, commit=False, session=session)
                    break
            else:
                to_create.append(datum)
        if commit:
            await session.commit()
            if refresh:
                for result in results:
                    await session.refresh(result)
        return to_create, unseen, results

    @classmethod
    async def correlate(
        cls,
        objs: list[Self],
        data: list[dict] | list[Self],
        on: Collection[str],
        *,
        update_fields: Collection[str] | None = None,
        commit: bool = True,
        refresh: bool = False,
        session: AsyncSession,
        **addl_data,
    ) -> list[Self]:
        if all(isinstance(datum, cls) for datum in data):
            # short-circuit if already correlated
            return data
        to_create, _, results = await cls._correlate(
            objs,
            data,
            on,
            update_fields=update_fields,
            session=session,
            commit=commit,
            refresh=refresh,
            **addl_data,
        )
        if to_create:
            results.extend(
                await cls.batch_create(
                    to_create,
                    session=session,
                    commit=commit,
                    refresh=refresh,
                    **addl_data,
                ),
            )
        return results
