import os
from dotenv import load_dotenv


load_dotenv()

class Config:
    SECRET_KEY = os.getenv('APP_SECRET')


class Dev(Config):
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.abspath(os.getcwd())}/dev.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Prod(Config):
    pass


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
