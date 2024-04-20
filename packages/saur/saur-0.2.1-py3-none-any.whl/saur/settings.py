from __future__ import annotations
from types import SimpleNamespace
from typing import Callable, Awaitable, TYPE_CHECKING
from functools import cached_property, partial

from sqlalchemy.engine import URL, Engine, create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm.session import Session, sessionmaker

from pydantic_settings import BaseSettings, SettingsConfigDict

if TYPE_CHECKING:
    from sqlalchemy.sql.schema import MetaData
    import pandas as pd

DIALECTS = SimpleNamespace(
    postgres=SimpleNamespace(
        sync_drivers=["psycopg2", "pg8000"],
        async_drivers=["asyncpg"],
    ),
    mysql=SimpleNamespace(
        sync_drivers=["mysqlclient", "mysqldb", "pymysql"],
        async_drivers=[None],
    ),
    sqlite=SimpleNamespace(
        sync_drivers=[None],
        async_drivers=["aiosqlite"],
    ),
)


def database_url(
    dialect: str,
    host: str,
    port: int | None = None,
    username: str | None = None,
    password: str | None = None,
    database: str | None = None,
    driver: str | None = None,
    query: dict[str, str | list[str]] = {},  # noqa: B006
    *,
    sync: bool = True,
) -> str:
    # cf https://docs.sqlalchemy.org/en/20/core/engines.html#database-urls
    # 'dialect+driver://username:password@host:port/database'
    if driver is None:
        if not hasattr(DIALECTS, dialect):
            msg = f"Cannot infer driver for dialect {dialect}."
            raise ValueError(msg)
        dialect_drivers = getattr(DIALECTS, dialect)
        # auto select driver
        if sync:
            driver = dialect_drivers.sync_drivers[0]
        else:
            driver = dialect_drivers.async_drivers[0]
    if driver is None:
        drivername = dialect
    else:
        drivername = f"{dialect}+{driver}"
    return URL.create(
        drivername=drivername,
        username=username,
        password=password,
        host=host,
        port=port,
        database=database,
        query=query,
    ).render_as_string()


class DBSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="DB_")

    dialect: str
    host: str
    port: int | None = None  # port constraints?
    username: str | None = None
    password: str | None = None
    database: str | None = None
    driver: str | None = None
    echo: bool = False

    def url(self, *, sync: bool = True) -> URL:
        settings = self.model_dump()
        settings.pop("echo")
        return database_url(sync=sync, **settings)

    def create_engine(self, *, sync: bool = True, **kwargs) -> Engine:
        url = self.url(sync=sync)
        kwargs.setdefault("echo", self.echo)
        if sync:
            return create_engine(url, **kwargs)
        return create_async_engine(url, **kwargs)

    @cached_property
    def engine(self) -> Engine:
        return self.create_engine()

    def sessionmaker(
        self,
        *,
        sync: bool = True,
        engine: Engine | None = None,
        **kwargs,
    ) -> Session:
        if engine is None:
            engine = self.create_engine(sync=sync)
        return sessionmaker(engine, class_=Session if sync else AsyncSession, **kwargs)

    def read_sql(self, sql: str, **kwargs) -> pd.DataFrame:
        import pandas as pd

        return pd.read_sql(sql, con=self.engine, **kwargs)

    def create_all(
        self,
        metadata: MetaData,
        *,
        sync: bool = True,
        engine: Engine | None = None,
    ) -> Callable[[], Awaitable | None]:
        if engine is None:
            engine = self.create_engine(sync=sync)
        if sync:
            return partial(metadata.create_all, engine)

        async def async_create_all() -> None:
            async with engine.begin() as conn:
                await conn.run_sync(metadata.create_all)  # pylint: disable=no-member

        return async_create_all
