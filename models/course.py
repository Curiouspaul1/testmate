from main import db
from models.base import IdMixin
from enum import Enum

class MaterialTypeEnum(Enum):
    ARTICLE = 1
    VIDEO = 2
    TEXTBOOK = 3


class Course(db.Model, IdMixin):
    title = db.Column(db.String(50), nullable=False)
    no_of_units = db.Column(db.Integer, nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'))


class CourseMaterial(db.Model, IdMixin):
    type = db.Column(db.Enum(MaterialTypeEnum), nullable=False)
    src = db.Column(db.String())
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
