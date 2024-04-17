# pylint: disable=missing-module-docstring,missing-function-docstring,missing-class-docstring
from __future__ import annotations
from typing import Annotated, Collection, Callable
from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.sql.schema import MetaData
from fastapi import Depends, FastAPI #, Request
from fastapi.requests import HTTPConnection

from ..settings import DBSettings

__all__ = ["Session", "db_lifespan"]

#async def database_session(request: Request):
# HTTPConnection -> works for Request and Websocket
async def database_session(connection: HTTPConnection):
    session: AsyncSession = connection.state.sessionmaker()
    # for auto-commiting:
    # async with session.begin():
    #    yield session
    try:
        yield session
    #except:
        # await session.rollback()
    #    raise
    finally:
        await session.close()

Session = Annotated[AsyncSession, Depends(database_session)]

# pylint: disable=unused-argument
@asynccontextmanager
async def db_lifespan(
    app: FastAPI, settings: DBSettings | None = None,
    create_metadata: MetaData | Collection[MetaData] | None=None,
    init_hook: Callable | None=None,
    execution_options: dict | None=None, **kwargs,
):
    if settings is None:
        settings = DBSettings()
    engine = settings.create_engine(sync=False, execution_options=execution_options)
    app_sessionmaker = sessionmaker(engine, class_=AsyncSession, **kwargs)
    if create_metadata:
        async with engine.begin() as conn:
            try:
                metadatas = list(create_metadata)
            except TypeError:
                metadatas = [create_metadata]
            for metadata in metadatas:
                await conn.run_sync(metadata.create_all)
    if init_hook is not None:
        async with app_sessionmaker() as session:
            await init_hook(session)
    yield {
        "engine": engine,
        "sessionmaker": app_sessionmaker,
    }
