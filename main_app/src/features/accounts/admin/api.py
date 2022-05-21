from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer

from main_app.src.core.database import admin_collection
from main_app.src.core.settings import ADMIN_TOKEN
from main_app.src.features.accounts.admin.schema import Admin, AdminSignIn, AdminSingUp
from main_app.src.features.accounts.common.auth import JWTBearer
from main_app.src.features.accounts.common.utils import login_accout, signup_account

route = APIRouter(tags=['admin'], prefix='/admin')

oauth2 = OAuth2PasswordBearer(tokenUrl="token")


@route.post('/signup', response_model=Admin)
def create_admin(request: AdminSingUp):
    # token=Depends(oauth2)):
    return signup_account(request, 'admin')


@route.post('/login')
def admin_login(request: AdminSignIn):
    return login_accout(admin_collection, request, ADMIN_TOKEN)


@route.get('/admin-staff', dependencies=[Depends(JWTBearer(credentials_type=ADMIN_TOKEN))])
def admin_staff():
    return {"mess": "good"}
