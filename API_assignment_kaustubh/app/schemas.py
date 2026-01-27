from pydantic import BaseModel

class NoteBase(BaseModel):
    title: str
    description: str
    is_completed: bool

class NoteCreate(NoteBase):
    pass

class NoteUpdate(NoteBase):
    pass

class NoteResponse(NoteBase):
    id: int

    class Config:
        orm_mode = True
