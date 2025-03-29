from typing import Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.db.models import Settings


class CRUDSettings(CRUDBase[Settings]):
    def get_by_student(self, db: Session, student_id: int) -> Optional[Settings]:
        return db.query(self.model).filter(self.model.student_id == student_id).first()

    def update_notifications(
        self, db: Session, *, db_obj: Settings,
        notify_likes: bool = None, notify_messages: bool = None
    ) -> Settings:
        update_data = {}
        if notify_likes is not None:
            update_data["notify_likes"] = notify_likes
        if notify_messages is not None:
            update_data["notify_messages"] = notify_messages
        return self.update(db, db_obj=db_obj, obj_in=update_data)

settings = CRUDSettings(Settings)