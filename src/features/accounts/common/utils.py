from fastapi import HTTPException
from passlib.context import CryptContext

from src.core.crud import find_one_by_attr
from src.core.database import admin_collection, user_collection
from src.features.accounts.admin.crud import create_admin_crud
from src.features.accounts.common.auth import sign_jwt
from src.features.accounts.user.crud import create_user_crud

hash_helper = CryptContext(schemes=['bcrypt'])

CREATE_ACCOUNT = {
    "admin": {"func": create_admin_crud, "col": admin_collection},
    "user": {"func": create_user_crud, "col": user_collection}
}


def login_accout(accout_collection, request, token_type):
    accout_exist = find_one_by_attr(accout_collection, 'email', request.email)

    if accout_exist:
        password = hash_helper.verify(
            request.password, accout_exist.get('password')
        )
        if password:
            return sign_jwt(request.email, token_type)

        raise HTTPException(
            status_code=403,
            detail="Incorrect email"
        )
    raise HTTPException(
        status_code=403,
        detail="Incorrect email or password"
    )


def signup_account(request, account_type):
    collection = CREATE_ACCOUNT[account_type]['col']
    account_exist = find_one_by_attr(collection, 'email', request.email)
    if account_exist:
        raise HTTPException(
            status_code=400,
            detail="Account already exist"
        )
    request.password = hash_helper.encrypt(request.password)
    return CREATE_ACCOUNT[account_type]['func'](request)
