from datetime import datetime

from pydantic import BaseModel


class LikeBase(BaseModel):
    sender_id: int
    receiver_id: int
    status: bool  # True - лайк, False - дизлайк

class LikeCreate(LikeBase):
    pass

class LikeResponse(LikeBase):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True