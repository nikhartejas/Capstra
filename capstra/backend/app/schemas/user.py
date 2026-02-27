from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    risk_profile: str
    capital_amount: float
    experience_level: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr
    risk_profile: str
    capital_amount: float
    experience_level: str
    discipline_score: int

    class Config:
        from_attributes = True
