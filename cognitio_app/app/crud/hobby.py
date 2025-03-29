# from typing import Optional
#
# from sqlalchemy.orm import Session
#
# from app.crud.base import CRUDBase
# from app.db.models import Hobby
#
# class CRUDHobby(CRUDBase[Hobby]):
#     def get_by_name(self, db: Session, name: str) -> Optional[Hobby]:
#         return db.query(self.model).filter(self.model.hobby_name == name).first()
#
#     def update_name(self, db: Session, *, db_obj: Hobby, new_name: str) -> Hobby:
#         return self.update(db, db_obj=db_obj, obj_in={"hobby_name": new_name})
#
# hobby = CRUDHobby(Hobby)