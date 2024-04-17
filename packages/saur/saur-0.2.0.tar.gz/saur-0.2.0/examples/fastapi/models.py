# pylint: disable=missing-module-docstring,missing-function-docstring,missing-class-docstring
from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from saur.mixins.async_access import AsyncAccessMixin

class Base(DeclarativeBase):
    pass

class User(Base, AsyncAccessMixin):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    passhash: Mapped[str]
    salt: Mapped[str]
    notes: Mapped[list['Note']] = relationship(back_populates='user')

class Note(Base, AsyncAccessMixin):
    __tablename__ = "notes"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped[User] = relationship(back_populates='notes')
    title: Mapped[str]
    content: Mapped[str]
