from main import db


class IdMixin:
    id = db.Column(db.Integer, primary_key=True)
