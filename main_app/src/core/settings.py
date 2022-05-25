import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

MONGODB_PASSWORD = os.environ.get("MONGODB_PWD")
CONNECTION_STRING = f"mongodb+srv://michallasia:{MONGODB_PASSWORD}@cluster0.ifehq.mongodb.net/?retryWrites=true&w=majority"

APP_NAME = "TouristWiki"
SERVER_ADDRESS = os.environ.get("MAIN_APP_HOST")
SERVER_PORT = int(os.environ.get("MAIN_APP_PORT"))
DEBUG = int(os.environ.get("DEBUG"))

ADMIN_TOKEN = os.environ.get("ADMIN_TOKEN")
USER_TOKEN = os.environ.get("USER_TOKEN")

CREDENTIALS = {
    ADMIN_TOKEN: [ADMIN_TOKEN, USER_TOKEN],
    USER_TOKEN: [USER_TOKEN]
}
