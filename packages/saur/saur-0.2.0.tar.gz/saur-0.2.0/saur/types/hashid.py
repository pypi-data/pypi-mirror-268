# pylint: disable=missing-module-docstring,missing-function-docstring,missing-class-docstring
from typing import Self
from sqlalchemy.types import TypeDecorator, Integer
from sqlalchemy.dialects.postgresql import JSONB

import randseq

class StringInteger(TypeDecorator):
    # no-op type as fallback for undefined HashID
    impl = Integer
    python_type = str
    cache_ok = True

    def __init__(self, nullable: bool=True):
        self.nullable = nullable
        super().__init__()

    def process_bind_param(self, value: str | None, dialect) -> int | None:
        if self.nullable and value is None:
            return None
        return int(value)

    def process_result_value(self, value: int | None, dialect) -> str | None:
        if self.nullable and value is None:
            return None
        return str(value)

class HashID(TypeDecorator):
    impl = Integer
    python_type = str
    cache_ok = True

    @classmethod
    def loads(cls, spec: str | None, nullable: bool=True) -> Self | StringInteger:
        if spec is None:
            return StringInteger(nullable=nullable)
        hashid = HashID.loads(spec)
        return cls(**hashid.to_dict(), nullable=nullable)

    def __init__(
        self,
        bound: int,
        init: int,
        prog: int,
        alphabet: str,
        outlen: int,
        nullable: bool=True,
    ):
        self.hashid = randseq.HashID(
            bound=bound,
            init=init,
            prog=prog,
            alphabet=alphabet,
            outlen=outlen,
        )
        self.nullable = nullable
        super().__init__()

    def process_bind_param(self, value: str | None, dialect) -> int | None:
        if self.nullable and value is None:
            return None
        return self.hashid.invert(value)

    def process_result_value(self, value: int | None, dialect) -> str | None:
        if self.nullable and value is None:
            return None
        return self.hashid.hash(value)
