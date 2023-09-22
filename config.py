import os
from dotenv import load_dotenv
from datetime import timedelta


load_dotenv()

class Config:
    SECRET_KEY = os.getenv('APP_SECRET')
    JWT_COOKIE_SECURE = False
    JWT_TOKEN_LOCATION = ['cookies']
    JWT_SECRET_KEY = SECRET_KEY
    JWT_CSRF_IN_COOKIES = True
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)


class Dev(Config):
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.abspath(os.getcwd())}/dev.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Prod(Config):
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.abspath(os.getcwd())}/dev.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Test(Config):
    pass


options = {
    'default': Dev,
    'dev': Dev,
    'development': Dev,
    'prod': Prod,
    'production': Prod,
    'test': Test,
    'testing': Test
}
