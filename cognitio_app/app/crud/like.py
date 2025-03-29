from typing import List

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.db.models import Like


class CRUDLike(CRUDBase[Like]):
    def get_by_sender(self, db: Session, sender_id: int) -> List[Like]:
        return db.query(self.model).filter(self.model.sender_id == sender_id).all()

    def get_by_receiver(self, db: Session, receiver_id: int) -> List[Like]:
        return db.query(self.model).filter(self.model.receiver_id == receiver_id).all()

    def update_status(self, db: Session, *, db_obj: Like, new_status: bool) -> Like:
        return self.update(db, db_obj=db_obj, obj_in={"status": new_status})

like = CRUDLike(Like)