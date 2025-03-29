from pydantic import BaseModel


class TechnologyBase(BaseModel):
    tech_name: str

class TechnologyCreate(TechnologyBase):
    pass

class TechnologyResponse(TechnologyBase):
    id: int

    class Config:
        from_attributes = True