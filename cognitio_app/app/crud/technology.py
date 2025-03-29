from typing import Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.db.models import Technology


class CRUDTechnology(CRUDBase[Technology]):
    def get_by_name(self, db: Session, name: str) -> Optional[Technology]:
        return db.query(self.model).filter(self.model.tech_name == name).first()

    def update_name(self, db: Session, *, db_obj: Technology, new_name: str) -> Technology:
        return self.update(db, db_obj=db_obj, obj_in={"tech_name": new_name})

technology = CRUDTechnology(Technology)