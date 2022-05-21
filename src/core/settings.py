import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

MONGODB_PASSWORD = os.environ.get("MONGODB_PWD")
CONNECTION_STRING = f"mongodb+srv://michallasia:{MONGODB_PASSWORD}@cluster0.ifehq.mongodb.net/?retryWrites=true&w=majority"

APP_NAME = "TouristWiki"
SERVER_ADDRESS = "0.0.0.0"
SERVER_PORT = 8080
DEBUG = int(os.environ.get("DEBUG"))