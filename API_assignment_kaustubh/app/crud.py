from sqlalchemy.orm import Session
from . import models, schemas

#creating a note , POST
def create_note(db: Session, note: schemas.NoteCreate):
    db_note = models.Note(
        title=note.title,
        description=note.description,
        is_completed=note.is_completed
    )
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

#fetch all notes , GET
def get_all_notes(db: Session):
    return db.query(models.Note).all()

#modify a note , PUT
def update_note(db: Session, note_id: int, note: schemas.NoteUpdate):
    db_note = db.query(models.Note).filter(models.Note.id == note_id).first()

    if not db_note:
        return None

    db_note.title = note.title
    db_note.description = note.description
    db_note.is_completed = note.is_completed

    db.commit()
    db.refresh(db_note)
    return db_note

#delete a note , DELETE
def delete_note(db: Session, note_id: int):
    db_note = db.query(models.Note).filter(models.Note.id == note_id).first()

    if not db_note:
        return None

    db.delete(db_note)
    db.commit()
    return db_note
