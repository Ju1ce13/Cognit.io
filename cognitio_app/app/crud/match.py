from typing import List

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.db.models import Match


class CRUDMatch(CRUDBase[Match]):
    def get_by_user(self, db: Session, user_id: int) -> List[Match]:
        return db.query(self.model).filter(
            (self.model.student1_id == user_id) |
            (self.model.student2_id == user_id)
        ).all()

match = CRUDMatch(Match)