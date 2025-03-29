from sqlalchemy.orm import Session
from app.db.models import Student
from app.schemas.student import StudentCreate
from app.crud.base import CRUDBase

class CRUDStudent(CRUDBase[Student]):
    def create_with_tech(self, db: Session, *, obj_in: StudentCreate) -> Student:
        db_obj = Student(
            full_name=obj_in.full_name,
            age=obj_in.age,
            description=obj_in.description,
            city_id=obj_in.city_id
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

student = CRUDStudent(Student)