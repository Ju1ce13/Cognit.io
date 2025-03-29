from typing import List, Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.db.models import Photo


class CRUDPhoto(CRUDBase[Photo]):
    def get_by_student(self, db: Session, student_id: int) -> List[Photo]:
        return db.query(self.model).filter(self.model.student_id == student_id).all()

    def get_main_photo(self, db: Session, student_id: int) -> Optional[Photo]:
        return db.query(self.model).filter(
            self.model.student_id == student_id,
            self.model.is_main == True
        ).first()

    def set_as_main(self, db: Session, *, db_obj: Photo) -> Photo:
        # Сбрасываем главное фото если было
        if main_photo := self.get_main_photo(db, db_obj.student_id):
            self.update(db, db_obj=main_photo, obj_in={"is_main": False})
        return self.update(db, db_obj=db_obj, obj_in={"is_main": True})

photo = CRUDPhoto(Photo)