from fastapi.security import HTTPBasicCredentials

from pydantic import BaseModel, EmailStr


class SignIn(HTTPBasicCredentials):
    pass


class User(BaseModel):
    username: str
    password: str


class UserSinUp(User):
    email: EmailStr
