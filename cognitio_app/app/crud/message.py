from typing import List

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.db.models import Message


class CRUDMessage(CRUDBase[Message]):
    def get_by_chat(self, db: Session, chat_id: int) -> List[Message]:
        return db.query(self.model).filter(
            self.model.chat_id == chat_id
        ).order_by(self.model.sent_at).all()

    def update_content(self, db: Session, *, db_obj: Message, new_content: str) -> Message:
        return self.update(db, db_obj=db_obj, obj_in={"content": new_content})

message = CRUDMessage(Message)