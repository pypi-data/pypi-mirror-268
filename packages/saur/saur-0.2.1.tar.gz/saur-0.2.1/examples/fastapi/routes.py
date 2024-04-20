# pylint: disable=missing-module-docstring,missing-function-docstring,missing-class-docstring
from fastapi import APIRouter, Depends, status

from saur.app.fastapi import Session

from .auth import CurrentUser
from .models import Note
from .schemas import NoteSchema, NotesQuerySchema, NoteWritableSchema

notes_router = APIRouter(prefix="/note", tags=["notes"])

@notes_router.get("/", response_model=list[NoteSchema])
async def list_notes(
    current_user: CurrentUser, session: Session, query: NotesQuerySchema = Depends(),
):
    return await Note.find(session=session, user_id=current_user.id, **query.model_dump())

@notes_router.post("/", status_code=status.HTTP_200_OK)
async def create_note(current_user: CurrentUser, session: Session, note: NoteWritableSchema) -> int:
    note = Note.create(session=session, user_id=current_user.id, **note.model_dump())
    await session.commit()
    return note.id

@notes_router.get("/{note_id}", response_model=NoteSchema)
async def get_note(current_user: CurrentUser, session: Session, note_id: int):
    return await Note.get(note_id, user_id=current_user.id, session=session)

@notes_router.put("/{note_id}", response_model=NoteSchema, status_code=status.HTTP_205)
async def update_note(
    current_user: CurrentUser, session: Session, note_id: int, note: NoteWritableSchema,
):
    existing = await Note.get(note_id, user_id=current_user.id, session=session)
    existing.update(session=session, **note.model_dump())
    await session.commit()

@notes_router.delete("/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_note(current_user: CurrentUser, session: Session, note_id: int):
    existing = await Note.get(note_id, user_id=current_user.id, session=session)
    await existing.delete(session=session)
