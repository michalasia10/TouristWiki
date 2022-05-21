from typing import List

from fastapi import APIRouter, HTTPException
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

from src.core.crud import find_one_by_attr
from src.core.database import admin_collection
from src.features.accounts.admin.crud import create_admin_crud
from src.features.accounts.admin.schema import Admin
from src.features.accounts.common.auth import sign_jwt
from src.features.accounts.common.schema import SignIn, User
from src.features.accounts.common.schema import UserSinUp

route = APIRouter(tags=['admin'], prefix='/admin')

hash_helper = CryptContext(schemes=['bcrypt'])

oauth2 = OAuth2PasswordBearer(tokenUrl="token")


@route.post('/signup', response_model=User)
def create_admin(user: UserSinUp):
    admin_exist = find_one_by_attr(admin_collection, 'email', user.email)
    if admin_exist:
        raise HTTPException(
            status_code=400,
            detail="Admin already exist"
        )
    user.password = hash_helper.encrypt(user.password)
    return create_admin_crud(user)


@route.post('/login')
def admin_login(credentials: SignIn):
    admin_exist = find_one_by_attr(admin_collection, 'email', credentials.username)
    if admin_exist:
        password = hash_helper.verify(
            credentials.password, admin_exist.get('password')
        )
        if password:
            return sign_jwt(credentials.username)

        raise HTTPException(
            status_code=403,
            detail="Incorrect email"
        )
    raise HTTPException(
        status_code=403,
        detail="Incorrect email or password"
    )
