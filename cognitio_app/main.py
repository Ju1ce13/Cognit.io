from fastapi import FastAPI
from app.api.v1.endpoints import students
from app.db.session import engine
from app.db.models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(
    students.router,
    prefix="/api/v1/students",
    tags=["students"]
)