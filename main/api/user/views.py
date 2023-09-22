from . import user
from main import db
from schemas.users import (
    UserSignUpSchema,
    UserSchema
)
from models.users import Role

from flask import (
    request
)
from loguru import logger


@user.post('/')
def sign_up():
    schema = UserSignUpSchema()
    data = request.get_json(force=True)
    try:
        new_user = schema.load(data)
        # persist to database
        try:
            db.session.add(new_user)
            db.session.commit()

            resp = UserSchema().dump(new_user)

        except Exception as e:
            logger.error(e)
            db.session.rollback()
        finally:
            db.session.close()
    
    except Exception as e:
        return {
            'status': 'error',
            'message': str(e),
            'data': {}
        }


    return {
        'status': 'success',
        'message': 'sign up successful',
        'data': resp
    }, 201


@user.patch('/')
def update_info():
    pass
