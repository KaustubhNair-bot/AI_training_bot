from sqlalchemy import Column, Integer, String, Boolean
from .database import Base

class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(String(500))
    is_completed = Column(Boolean, default=False)
