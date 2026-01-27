from fastapi import FastAPI

from .database import engine
from . import models
from .routers import notes

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Todo Notes API")

@app.get("/")
def root():
    return {"message": "Welcome to the Todo Notes API 🚀"}

app.include_router(notes.router)
