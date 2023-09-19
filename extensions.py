from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS


ma = Marshmallow()
db = SQLAlchemy()
migrate = Migrate()
cors = CORS()
