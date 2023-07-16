from fastapi import FastAPI

from app.api import notes
from app import models
from .database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(notes.router, prefix="/api/notes", tags=["notes"])


@app.get("/api/healthcheck")
def root():
    return {"message": "Welcome to FastAPI CRUD Server"}
