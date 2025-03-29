from pydantic import BaseModel


class SettingsBase(BaseModel):
    student_id: int
    private_profile: bool = False
    notify_likes: bool = True
    notify_messages: bool = True

class SettingsCreate(SettingsBase):
    pass

class SettingsResponse(SettingsBase):
    id: int

    class Config:
        from_attributes = True