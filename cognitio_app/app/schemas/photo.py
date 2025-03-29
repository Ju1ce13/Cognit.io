from pydantic import BaseModel


class PhotoBase(BaseModel):
    student_id: int
    url: str
    is_main: bool = False

class PhotoCreate(PhotoBase):
    pass

class PhotoResponse(PhotoBase):
    id: int

    class Config:
        from_attributes = True