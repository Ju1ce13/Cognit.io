from typing import Optional, List

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.db.models import Chat, Match


class CRUDChat(CRUDBase[Chat]):
    def get_by_match(self, db: Session, match_id: int) -> Optional[Chat]:
        return db.query(self.model).filter(self.model.match_id == match_id).first()

    def get_by_user(self, db: Session, user_id: int) -> List[Chat]:
        return db.query(self.model).join(Match).filter(
            (Match.student1_id == user_id) |
            (Match.student2_id == user_id)
        ).all()

chat = CRUDChat(Chat)