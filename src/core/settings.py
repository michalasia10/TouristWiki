import os
from dotenv import load_dotenv,find_dotenv

load_dotenv(find_dotenv())

MONGODB_PASSWORD = os.environ.get("MONGODB_PWD")
CONNECTION_STRING = ""
