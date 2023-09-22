from flask import Flask
from config import options
from extensions import (
    ma, db, cors, bcrypt,
    jwt
)
from dotenv import load_dotenv
from flask_jwt_extended import get_jwt
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import create_access_token
from flask_jwt_extended import set_access_cookies

import os
import datetime
from datetime import (
    timezone,
    timedelta,
    datetime
)

load_dotenv()


app = Flask(__name__)

app.config.from_object(options[os.getenv('APP_ENV', 'default')])

# init extensions
ma.init_app(app)
db.init_app(app)
jwt.init_app(app)
cors.init_app(app)
bcrypt.init_app(app)

# register blueprints
from .api import api

app.register_blueprint(api)


@app.errorhandler(404)
def route_not_found(error):
    return "Resource/page not found 💀 - wetin u dey dooo", 404

@app.after_request
def refresh_expiring_jwts(response):
    try:
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
            set_access_cookies(response, access_token)
        return response
    except (RuntimeError, KeyError):
        # Case where there is not a valid JWT. Just return the original response
        return response
