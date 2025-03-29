from datetime import datetime

from pydantic import BaseModel


class MatchBase(BaseModel):
    student1_id: int
    student2_id: int

class MatchCreate(MatchBase):
    pass

class MatchResponse(MatchBase):
    id: int
    match_date: datetime

    class Config:
        from_attributes = True