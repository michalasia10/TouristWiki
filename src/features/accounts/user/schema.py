from pydantic import BaseModel, EmailStr


class User(BaseModel):
    user: str
    pwd: str


class UserSinUp(User):
    email: EmailStr
