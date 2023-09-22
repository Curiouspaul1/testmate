from flask import Blueprint


api = Blueprint('api', __name__, url_prefix='/api')


from .assessments import assess
from .course import courses
from .students import student
from .teachers import teacher
from .schools import school
from .auth import auth
from .user import user

api.register_blueprint(courses)
api.register_blueprint(assess)
api.register_blueprint(student)
api.register_blueprint(teacher)
api.register_blueprint(user)
api.register_blueprint(auth)
api.register_blueprint(school)
