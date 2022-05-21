from src.core.database import db
from src.features.accounts.user.schema import UserSinUp
from fastapi.encoders import jsonable_encoder


def create_user_crud(user: UserSinUp):
    db.command("createUser", jsonable_encoder(user))
