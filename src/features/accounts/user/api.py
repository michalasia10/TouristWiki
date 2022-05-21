from fastapi import APIRouter

from src.core.database import user_collection
from src.core.settings import USER_TOKEN
from src.features.accounts.common.utils import login_accout, signup_account
from src.features.accounts.user.schema import NormalUser, NormalUserSignIn, NormalUserSinUp

route = APIRouter(tags=['user'], prefix='/user')


@route.post('/signup', response_model=NormalUser)
def create_user(request: NormalUserSinUp, ):
    return signup_account(request, 'user')


@route.post('/login')
def user_login(request: NormalUserSignIn):
    return login_accout(user_collection, request, USER_TOKEN)
