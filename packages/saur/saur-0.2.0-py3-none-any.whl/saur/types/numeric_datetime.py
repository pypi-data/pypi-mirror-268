# pylint: disable=missing-module-docstring,missing-function-docstring,missing-class-docstring
from datetime import datetime, timedelta, timezone
from typing import Union

from sqlalchemy.types import TypeDecorator
from sqlalchemy import Integer, Float

# as numeric b/c dateinterval logic is not supported by sqlalchemy across dialects
class FloatDateTime(TypeDecorator):
    impl = Float
    python_type = datetime
    cache_ok = True
    def process_bind_param(self, value: datetime, dialect) -> int:
        if value is None:
            return None
        # all datetimes are UTC
        return value.replace(tzinfo=timezone.utc).timestamp()

    def process_result_value(self, value, dialect):
        if value is None:
            return None
        return datetime.utcfromtimestamp(value)
        # all datetimes are UTCtcfromtimestamp(value)

    def coerce_compared_value(self, op, value):
        if isinstance(value, float):
            return Float()
        elif isinstance(value, int):
            return Integer()
        else:
            return self

    def __repr__(self):
        return "FloatDateTime"

class IntDateTime(FloatDateTime):
    impl = Integer
    def process_bind_param(self, value: datetime, dialect) -> float:
        if value is None:
            return None
        return int(super().process_bind_param(value, dialect))

    def __repr__(self):
        return "IntDateTime"

class FloatTimeDelta(TypeDecorator):
    impl = Float
    python_type = timedelta
    cache_ok = True
    def process_bind_param(self, value: Union[timedelta, float, int, None], dialect) -> float:
        if value is None:
            return None
        if isinstance(value, (float, int)):
            return value
        return timedelta.total_seconds(value)

    def process_result_value(self, value, dialect) -> timedelta:
        if value is None:
            return None
        return timedelta(seconds=value)

    def coerce_compared_value(self, op, value):
        if isinstance(value, float):
            return Float()
        elif isinstance(value, int):
            return Integer()
        else:
            return self
    def __repr__(self):
        return "FloatTimeDelta"

class IntTimeDelta(FloatTimeDelta):
    impl = Integer
    def process_bind_param(self, value: Union[timedelta, float, int], dialect) -> int:
        if isinstance(value, (float, int)):
            return int(value)
        return int(super().process_bind_param(value, dialect))
    def __repr__(self):
        return "IntTimeDelta"
