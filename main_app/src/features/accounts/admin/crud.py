from bson import ObjectId
from fastapi.encoders import jsonable_encoder

from main_app.src.core.crud import find_by_objectid
from main_app.src.core.database import admin_collection


def create_admin_crud(admin):
    obj_id: ObjectId = admin_collection.insert_one(jsonable_encoder(admin)).inserted_id
    return find_by_objectid(admin_collection, obj_id)
