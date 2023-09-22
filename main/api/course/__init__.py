from flask import Blueprint


courses = Blueprint('course', __name__, url_prefix='/courses')

from . import views
