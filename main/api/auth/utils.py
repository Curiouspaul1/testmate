from models import User

from functools import wraps
from flask import (
    abort,
    make_response
)
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)


def login_required(f):
    @jwt_required()
    def wrapper(*args, **kwargs):
        #TODO: add extra func
        uid = get_jwt_identity()
        
        # double check identity
        user = User.get_by_email(uid)
        if not user:
            resp = make_response({
                'status': 'error',
                'message': f'user with uid: {uid} not found',
                'data': None
            })
            abort(404, resp)
        return f(user, *args, **kwargs)
    return wrapper
