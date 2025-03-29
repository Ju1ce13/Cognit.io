from datetime import datetime

from pydantic import BaseModel


class MessageBase(BaseModel):
    chat_id: int
    sender_id: int
    content: str

class MessageCreate(MessageBase):
    pass

class MessageResponse(MessageBase):
    id: int
    sent_at: datetime

    class Config:
        from_attributes = True