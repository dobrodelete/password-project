import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'
    FERNET_KEY = os.environ.get('FERNET_KEY').encode()


config = Config()
