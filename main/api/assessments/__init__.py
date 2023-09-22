from flask import Blueprint


assess = Blueprint('assess', __name__, url_prefix='/assessment')

from . import views
