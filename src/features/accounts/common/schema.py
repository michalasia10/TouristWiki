from pydantic import BaseModel, EmailStr


class UserSignIn(BaseModel):
    email: EmailStr
    password: str


class User(BaseModel):
    username: str
    password: str


class UserSingUp(User):
    email: EmailStr
