from bson import ObjectId
from fastapi.encoders import jsonable_encoder

from src.core.crud import find_by_objectid
from src.core.database import user_collection


def create_user_crud(user):
    obj_id: ObjectId = user_collection.insert_one(jsonable_encoder(user)).inserted_id
    return find_by_objectid(user_collection, obj_id)
