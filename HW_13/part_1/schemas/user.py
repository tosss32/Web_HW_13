from pydantic import BaseModel


class User(BaseModel):
    username: str
    email: str
    password: str
    is_verified: bool = False
    avatar_public_id: str = None

    class Config:
        from_attributes = True

class UserVerification(BaseModel):
    token: str

class UserUpdate(BaseModel):
    avatar_url: str
