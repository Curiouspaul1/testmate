from models.base import IdMixin
from main import db
from utils import (
    gen_token,
    slugify
)


class School(db.Model, IdMixin):
    name = db.Column(db.String(20))
    code = db.Column(
        db.String(15),
        nullable=False,
        unique=True
    )
    teachers = db.relationship('Teacher', backref='school')
    students = db.relationship('Student', backref='school')
    school_slug = db.Column(db.String(10), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def gen_code():
        pass
    
    def update_slug(self):
        self.school_slug = slugify(self.name)
    
    def update_code(self):
        self.code = gen_token(15, upper_case_only=True)

# class Class(db.Model, IdMixin):
