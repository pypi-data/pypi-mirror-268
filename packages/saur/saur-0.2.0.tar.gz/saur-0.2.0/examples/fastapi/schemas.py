# pylint: disable=missing-module-docstring,missing-function-docstring,missing-class-docstring

from pydantic import BaseModel

class NoteWritableSchema(BaseModel):
    title: str
    content: str

class NoteSchema(NoteWritableSchema):
    id: int
    user_id: int

class NotesQuerySchema(BaseModel):
    # nothing to query on
    pass

class UserWritableSchema(BaseModel):
    email: str
    password: str | None = None

class UserCreateSchema(UserWritableSchema):
    # password required on creation
    password: str
