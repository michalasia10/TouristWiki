import smtplib
from email.mime.text import MIMEText
from typing import List

from pydantic import EmailStr

from mail_app.src.settings import MAIL_SENDER, MAIL_PASSWORD, MAIL_SERVER, MAIL_PORT


async def send_email(receivers: List[EmailStr], subject, html_body, **kwargs):
    receivers = ', '.join(receivers)
    sm = smtplib.SMTP(MAIL_SERVER, MAIL_PORT)
    sm.ehlo()
    sm.starttls()
    sm.login(MAIL_SENDER, MAIL_PASSWORD)

    mail = MIMEText(str(html_body, "UTF-8"), 'html')
    mail['Subject'] = subject
    mail['From'] = MAIL_SENDER
    mail['To'] = receivers

    try:
        sm.sendmail(MAIL_SENDER, receivers, mail.as_string())
        sm.close()
    except Exception as e:
        return e
