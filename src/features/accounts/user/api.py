from fastapi import APIRouter

from src.features.accounts.user.crud import create_user_crud
from src.features.accounts.user.schema import UserSinUp,User

route = APIRouter(tags=['user'], prefix='/user')


@route.post('/create', response_model=User)
def create_user(user: UserSinUp):
    return create_user_crud(user)
