from main import ma


class AdminLogin(ma.Schema):
    email = ma.Email(required=True)
    password = ma.String(required=True)
