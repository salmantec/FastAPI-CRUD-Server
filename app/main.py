from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import notes
from app import models
from .database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(notes.router, prefix="/api/notes", tags=["notes"])


@app.get("/api/healthcheck")
def root():
    return {"message": "Welcome to FastAPI CRUD Server"}
