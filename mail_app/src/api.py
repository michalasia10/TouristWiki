from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.templating import Jinja2Templates
from starlette.responses import JSONResponse

from mail_app.src import utils
from mail_app.src.schema import WelcomeMail

router = APIRouter(tags=['email'], prefix='/email')

templates = Jinja2Templates(directory='mail_app/src/templates/')


@router.post('/send-welcome-mail')
async def send_email(email: WelcomeMail):
    serializer:dict = jsonable_encoder(email)
    body_args:dict = serializer.get("body_args")

    context = {"request": ""}
    context.update(body_args)

    body_html = templates.TemplateResponse("welcome_mail.html", context).body

    await utils.send_email(html_body=body_html, **jsonable_encoder(email))
    return JSONResponse(status_code=200, content={"message": "email has been sent"})
