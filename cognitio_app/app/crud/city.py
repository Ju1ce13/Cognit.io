from typing import Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.db.models import City


class CRUDCity(CRUDBase[City]):
    def get_by_name(self, db: Session, name: str) -> Optional[City]:
        return db.query(self.model).filter(self.model.city_name == name).first()

    def update_name(self, db: Session, *, db_obj: City, new_name: str) -> City:
        return self.update(db, db_obj=db_obj, obj_in={"city_name": new_name})

city = CRUDCity(City)