# adapted from https://sqlalchemy-utils.readthedocs.io/en/latest/_modules/sqlalchemy_utils/types/scalar_list.html#ScalarListType
from __future__ import annotations
from sqlalchemy.types import UnicodeText, TypeDecorator


class DelimitedList(TypeDecorator):
    impl = UnicodeText()
    cache_ok = True

    def __init__(self, serialize=None, deserialize=None, separator: str = ","):
        self.separator = separator
        self.serialize = serialize
        self.deserialize = deserialize
        super().__init__()

    def process_bind_param(self, value: list | None, dialect):
        if value is None:
            return None

        if self.serialize:
            serialized_values = [self.serialize(val) for val in value]
        else:
            serialized_values = value
        invalid_values = [val for val in serialized_values if self.separator in val]
        if invalid_values:
            msg = f"Delimited values {invalid_values!r} cannot contain seperator {self.separator!r}"
            raise ValueError(msg)
        return self.separator.join(serialized_values)

    def process_result_value(self, value: str | None, dialect) -> list:
        if value is None:
            return None
        if not value:
            return []

        if self.deserialize:
            return [self.deserialize(val) for val in value.split(self.separator)]
        return list(value.split(self.separator))
