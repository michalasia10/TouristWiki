from bson import ObjectId
from pymongo.collection import Collection

from src.core.database import db

def get_all(collection:Collection):
    return collection.find()

def find_by_objectid(collection: Collection, obj_id: ObjectId):
    return collection.find_one(obj_id)


def find_one_by_attr(collection: Collection, attr, value):
    if not collection.name in db.list_collection_names():
        collection.insert_one({
            "user": "string",
            "pwd": "string",
            "email": "user@example.com"
        })
    return collection.find_one({attr: value})
