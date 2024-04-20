# pylint: disable=missing-module-docstring,missing-function-docstring,missing-class-docstring
from dateutil.relativedelta import relativedelta

from sqlalchemy.types import TypeDecorator, JSON
from sqlalchemy.dialects.postgresql import JSONB
from pydantic import BaseModel

def not_private(attr: str):
    return not attr.startswith('_')

class RelativeDeltaModel(BaseModel):
    years: int = 0
    months: int = 0
    days: int = 0
    leapdays: int = 0
    hours: int = 0
    minutes: int = 0
    seconds: int = 0
    microseconds: int = 0
    year: int | None = None
    month: int | None = None
    day: int | None = None
    hour: int | None = None
    minute: int | None = None
    second: int | None = None
    microsecond: int | None = None
    weekday: int | None = None
    # _has_time: int ?

    def relativedelta(self):
        return relativedelta(**self.model_dump())

def _screen_values(delta: dict[str, int | None]):
    return {
        k: v for k, v in delta.items()
        if not (
            k.startswith("_") or
            v is None or
            (k.endswith("s") and v == 0)
        )
    }

def serialize_relativedelta(
    delta: relativedelta | RelativeDeltaModel | dict,
) -> dict[str, int | None]:
    if isinstance(delta, relativedelta):
        return _screen_values(delta.__dict__)
    if isinstance(delta, RelativeDeltaModel):
        return _screen_values(delta.model_dump())
    if isinstance(delta, dict):
        return _screen_values(delta)
    raise TypeError(f"Unknown type for relativedelta: {type(delta)}")

def deserialize_relativedelta(delta: dict[str, int | None]) -> relativedelta:
    return relativedelta(**delta)

class RelativeDelta(TypeDecorator):
    impl = JSON
    python_type = relativedelta
    cache_ok = True

    def __init__(self, nullable: bool=True):
        self.nullable = nullable
        super().__init__()

    def process_bind_param(self, value, dialect):
        if self.nullable and value is None:
            return None
        return serialize_relativedelta(value)

    def process_result_value(self, value, dialect):
        if self.nullable and value is None:
            return None
        return deserialize_relativedelta(value)

class RelativeDeltaB(RelativeDelta):
    def load_dialect_impl(self, dialect):
        if dialect.name == 'postgresql':
            return dialect.type_descriptor(JSONB())
        return dialect.type_descriptor(JSON())
