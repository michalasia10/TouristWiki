from pymongo import MongoClient
from pymongo.database import Database, Collection
from main_app.src.core.settings import CONNECTION_STRING, DEBUG

client = MongoClient(CONNECTION_STRING)

if DEBUG:
    db: Database = client.develop
else:
    db: Database = client.production

admin_collection: Collection = db.admin
user_collection: Collection = db.user
