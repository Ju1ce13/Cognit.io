from pydantic import BaseModel
from typing import Optional

class CityBase(BaseModel):
    city_name: str

class CityCreate(CityBase):
    pass

class CityResponse(CityBase):
    id: int

    class Config:
        from_attributes = True