from bson import ObjectId
from fastapi.encoders import jsonable_encoder

from src.core.crud import find_by_objectid
from src.core.database import admin_collection,db

def create_admin_crud(admin):
    obj_id: ObjectId = admin_collection.insert_one(jsonable_encoder(admin)).inserted_id
    return find_by_objectid(admin_collection, obj_id)
