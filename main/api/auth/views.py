from . import auth
from main import bcrypt
from models.users import User
from schemas.generic import AdminLogin
from schemas.users import UserSchema

from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_csrf_token
)
from flask import (
    request, jsonify,
    make_response
)
from loguru import logger


@auth.post('/')
def login():
    schema = AdminLogin()
    resp = {
        'message': None,
        'data': None,
        'status': None
    }

    data = request.get_json(force=True)

    try:
        data = schema.load(data)
    except Exception as e:
        logger.error(e)
        resp['message'] = str(e)
        resp['status'] = 'error'
        return resp, 400
    
    user: User = User.get_by_email(data['email'])
    if not user:
        resp['message'] = f"user with email {data['emai']} not found"
        resp['status'] = 'error'
        return resp, 404

    # compare passwords
    check: bool = bcrypt.check_password_hash(user.password, data['password'])
    if not check:
        resp['message'] = f"Incorrect password"
        resp['status'] = 'error'
        return resp, 401

    # gen token
    token = create_access_token(identity=user.email)

    resp = make_response(
        {
            'status': 'success',
            'message': 'login successful',
            'data': {}
        }, 200
    )
    resp.set_cookie('access_token_cookie', token)
    resp.set_cookie('csrf_access_token', get_csrf_token(token))

    return resp
