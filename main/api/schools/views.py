from main import db
from . import school
from schemas.school import SchoolSchema
from models.school import School
from main.api.auth.utils import login_required


from flask import request
from loguru import logger
# from flask_jwt_extended import jwt_required


@school.post('/')
@login_required
def add_new_school(current_user):
    data = request.get_json()
    resp = {
        'message': None,
        'data': None,
        'status': None
    }

    try:
        new_school: School = SchoolSchema().load(data)
    except Exception as e:
        logger.error(e)
        resp['message'] = str(e)
        resp['status'] = 'error'
        return resp, 400

    try:
        db.session.add(new_school)
        new_school.update_slug()
        new_school.update_code()

        new_school.owner = current_user
        db.session.commit()

        obj = SchoolSchema().dump(new_school)
    except Exception as e:
        logger.error(e)
        db.session.rollback()

        resp['message'] = str(e)
        resp['status'] = 'error'
        return resp, 500
    finally:
        db.session.close()

    resp['data'] =  obj
    resp['message'] = 'School created'
    resp['status'] = 'success'

    return resp
