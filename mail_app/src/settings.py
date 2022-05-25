import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

APP_NAME = "TouristWikiMailService"
SERVER_ADDRESS = os.environ.get("MAIL_APP_HOST")
SERVER_PORT = int(os.environ.get("MAIL_APP_PORT"))
DEBUG = int(os.environ.get("DEBUG"))

MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
MAIL_SENDER = os.environ.get("MAIL_ADDRESS")
MAIL_PORT = os.environ.get("MAIL_PORT")
MAIL_SERVER = os.environ.get("MAIL_SERVER")
