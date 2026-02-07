import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    SESSION_PERMANENT = False
    PERMANENT_SESSION_LIFETIME = int(os.getenv("SESSION_TIMEOUT"))