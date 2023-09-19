from flask import Flask
from config import options
from extensions import (
    ma, db, cors, migrate
)
from dotenv import load_dotenv

import os


load_dotenv()


app = Flask(__name__)

app.config.from_object(options[os.getenv('APP_ENV', 'default')])

# init extensions
ma.init_app(app)
db.init_app(app)
# migrate.init_app(app, db)
cors.init_app(app)


# register blueprints
from .assessments import assess
from .course import courses
from .students import student
from .teachers import teacher

app.register_blueprint(courses)
app.register_blueprint(assess)
app.register_blueprint(student)
app.register_blueprint(teacher)
