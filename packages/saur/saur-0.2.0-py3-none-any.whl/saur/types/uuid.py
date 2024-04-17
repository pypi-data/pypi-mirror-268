# adapted from https://stackoverflow.com/a/30604002
# and from https://sqlalchemy-utils.readthedocs.io/en/latest/_modules/sqlalchemy_utils/types/uuid.html#UUIDType
import uuid

from sqlalchemy.types import TypeDecorator, BINARY, CHAR
from sqlalchemy.dialects import postgresql, mssql

class UUID(TypeDecorator):
    """Platform-independent GUID type.

    Uses Postgresql's UUID type, otherwise uses
    BINARY(16), to store UUID.

    """
    impl = BINARY(16)
    python_type = uuid.UUID
    cache_ok = True

    def __init__(self, binary: bool=True, native: bool=True):
        self.binary = binary
        self.native = native
        super().__init__()

    def load_dialect_impl(self, dialect):
        if self.native:
            if dialect.name in ('postgresql', 'cockroachdb'):
                return dialect.type_descriptor(postgresql.UUID())
            if dialect.name == 'mssql':
                return dialect.type_descriptor(mssql.UNIQUEIDENTIFIER())
        impl = BINARY(16) if self.binary else CHAR(32)
        return dialect.type_descriptor(impl)

    def process_bind_param(self, value, dialect) -> None | str | bytes:
        if value is None:
            return value
        if not isinstance(value, uuid.UUID):
            if isinstance(value, bytes):
                value = uuid.UUID(bytes=value)
            elif isinstance(value, int):
                value = uuid.UUID(int=value)
            elif isinstance(value, str):
                value = uuid.UUID(value)
        if self.native and dialect.name in (
            'postgresql', 'mssql', 'cockroachdb',
        ):
            return str(value)
        return value.bytes if self.binary else value.hex

    def process_result_value(self, value, dialect) -> None | uuid.UUID:
        if value is None:
            return value
        if self.native and dialect.name in (
            'postgresql', 'mssql', 'cockroachdb',
        ):
            if isinstance(value, uuid.UUID):
                result = value
            else:
                result = uuid.UUID(value)
        elif self.binary:
            result = uuid.UUID(bytes=value)
        else:
            result = uuid.UUID(value)
        return result
