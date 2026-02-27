from pydantic import BaseModel


class MentorChatIn(BaseModel):
    user_id: int
    message: str
