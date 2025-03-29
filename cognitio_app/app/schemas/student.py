from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class TechnologyBase(BaseModel):
    name: str


class StudentBase(BaseModel):
    full_name: str
    age: int
    description: Optional[str] = None


class StudentCreate(StudentBase):
    technologies: List[str] = []
    hobbies: List[str] = []
    city_id: int


class StudentResponse(StudentBase):
    id: int
    technologies: List[TechnologyBase]
    created_at: datetime

    class Config:
        orm_mode = True