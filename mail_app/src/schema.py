from typing import List

from pydantic import BaseModel, EmailStr


class WelcomeArgs(BaseModel):
    username: str


class EmailSchema(BaseModel):
    subject: str
    receivers: List[EmailStr]
    body_args: dict


class WelcomeMail(EmailSchema):
    body_args: WelcomeArgs
