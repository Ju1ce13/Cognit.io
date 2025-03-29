from typing import Optional, List, Dict

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.crud.technology import technology
from app.db.models import Student


class CRUDStudent(CRUDBase[Student]):
    def get_by_name(self, db: Session, name: str) -> Optional[Student]:
        return db.query(self.model).filter(self.model.full_name == name).first()

    def create_with_relations(
        self, db: Session, *, obj_in: Dict,
        tech_names: List[str] = [], hobby_names: List[str] = []
    ) -> Student:
        db_obj = self.model(**obj_in)
        for tech_name in tech_names:
            if tech := technology.get_by_name(db, tech_name):
                db_obj.technologies.append(tech)
        for hobby_name in hobby_names:
            if hobby := hobby.get_by_name(db, hobby_name):
                db_obj.hobbies.append(hobby)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update_relations(
        self, db: Session, *, db_obj: Student,
        tech_names: List[str] = None, hobby_names: List[str] = None
    ) -> Student:
        if tech_names is not None:
            db_obj.technologies = []
            for tech_name in tech_names:
                if tech := technology.get_by_name(db, tech_name):
                    db_obj.technologies.append(tech)
        if hobby_names is not None:
            db_obj.hobbies = []
            for hobby_name in hobby_names:
                if hobby := hobby.get_by_name(db, hobby_name):
                    db_obj.hobbies.append(hobby)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

student = CRUDStudent(Student)