# pylint: disable=missing-module-docstring,missing-function-docstring,missing-class-docstring

from sqlalchemy.types import TypeDecorator, JSON
from sqlalchemy.dialects.postgresql import JSONB
from pydantic import BaseModel

class ModeledJSON(TypeDecorator):
    impl = JSON

    def __init__(self, model: BaseModel, nullable: bool=True, **dump_kwargs):
        self.model = model
        self.nullable = nullable
        # default to mode: json for types like datetimes
        self.dump_kwargs = dump_kwargs | {"mode": "json"}
        super().__init__()

    def process_bind_param(self, value, dialect):
        # TODO: make sure this accepted the pydantic type & valid raw data
        if self.nullable and value is None:
            return None
        modeled = self.model.model_validate(value)
        return modeled.model_dump(**self.dump_kwargs)

    def process_result_value(self, value, dialect):
        if self.nullable and value is None:
            return None
        return self.model.model_validate(value)

class ModeledJSONB(ModeledJSON):
    def load_dialect_impl(self, dialect):
        if dialect.name == 'postgresql':
            return dialect.type_descriptor(JSONB())
        return dialect.type_descriptor(JSON())
