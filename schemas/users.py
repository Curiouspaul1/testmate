from main import (
    ma,
    bcrypt
)
from models.users import User

from marshmallow import post_load


class UserSignUpSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True


    @post_load
    def hash_pass(self, user_obj, *args, **kwargs):
        if user_obj:
            user_obj['password'] = bcrypt.generate_password_hash(user_obj['password']).decode('utf-8')
        return user_obj


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

        exclude = ('password',)
