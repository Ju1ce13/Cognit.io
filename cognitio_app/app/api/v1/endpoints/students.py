from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.student import StudentCreate, StudentResponse
from app.crud.student import student
from app.db.session import get_db

router = APIRouter()

@router.post("/", response_model=StudentResponse)
def create_student(
    student_in: StudentCreate,
    db: Session = Depends(get_db)
):
    return student.create_with_tech(db, obj_in=student_in)

@router.get("/{student_id}", response_model=StudentResponse)
def read_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    db_student = student.get(db, id=student_id)
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student