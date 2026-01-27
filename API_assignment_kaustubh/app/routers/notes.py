from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..database import get_db

router = APIRouter(
    prefix="/notes",
    tags=["Notes"]
)

@router.post(
    "/",
    response_model=schemas.NoteResponse,
    status_code=status.HTTP_201_CREATED
)
def create_note(note: schemas.NoteCreate, db: Session = Depends(get_db)):
    return crud.create_note(db, note)

@router.get(
    "/",
    response_model=list[schemas.NoteResponse]
)
def get_all_notes(db: Session = Depends(get_db)):
    return crud.get_all_notes(db)

@router.put(
    "/{note_id}",
    response_model=schemas.NoteResponse
)
def update_note(
    note_id: int,
    note: schemas.NoteUpdate,
    db: Session = Depends(get_db)
):
    updated_note = crud.update_note(db, note_id, note)

    if not updated_note:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Note not found"
        )

    return updated_note

@router.delete(
    "/{note_id}",
    status_code=status.HTTP_200_OK
)
def delete_note(note_id: int, db: Session = Depends(get_db)):
    deleted_note = crud.delete_note(db, note_id)

    if not deleted_note:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Note not found"
        )

    return {"message": "Note deleted successfully"}
