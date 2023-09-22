from flask import Blueprint

school = Blueprint('school', __name__, url_prefix='/school')

from . import views
