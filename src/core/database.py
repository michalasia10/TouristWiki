from pymongo import MongoClient
from pymongo.database import Database, Collection
from src.core.settings import CONNECTION_STRING, DEBUG

client = MongoClient(CONNECTION_STRING)


db: Database = client.production

admin_collection: Collection = db.admin
user_collection: Collection = db.user
