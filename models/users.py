from main import db
from models.base import IdMixin
from utils import gen_token


class Permissions:
    ADD_SCHOOL = 2
    EDIT_SCHOOL = 4
    REMOVE_SCHOOL = 8
    ADD_TEACHER = 16
    REMOVE_TEACHER = 32
    VIEW_SCHOOL = 64
    AMDIN = 8192


class SchoolPermissions:
    # tutor perms
    ADD_COURSE = 128
    DELETE_COURSE = 256
    EDIT_COURSE = 512
    
    # student perms
    TAKE_COURSE = 1024
    TAKE_TEST = 2048
    SEE_RESULTS = 4096



class User(db.Model, IdMixin):
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(300))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    school = db.relationship('School', backref='owner', uselist=False)

    @classmethod
    def get_by_email(cls, email):
        return cls.query.filter_by(email=email).first()



class Student(db.Model, IdMixin):
    student_id = db.Column(
        db.String(8),
        nullable=False,
        unique=True,
        default=gen_token(8),
        index=True
    )
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    class_name = db.Column(db.String(20))
    school_id = db.Column(db.Integer, db.ForeignKey('school.id'))

    def update_gpa(self):
        pass

    def fetch_results(self):
        pass

    @classmethod
    def get_by_school_and_id(cls, student_id):
        pass



class Teacher(db.Model, IdMixin):
    teacher_id = db.Column(
        db.String(10),
        nullable=False,
        unique=True,
        default=gen_token(10),
        index=True
    )
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    courses = db.relationship('Course', backref='teacher')
    school_id = db.Column(db.Integer, db.ForeignKey('school.id'))


class Role(db.Model, IdMixin):
    name = db.Column(db.String(10))
    permissions = db.Column(db.Integer)
    users = db.relationship('User', backref='user')

    def has_perm(self, perm):
        return self.permissions & perm == perm
    
    def add_perm(self, perm):
        if not self.has_perm(perm):
            self.permissions += perm
    
    def remove_perm(self, perm):
        if self.has_perm(perm):
            self.permissions -= perm
    
    @staticmethod
    def create_roles():
        """
        Generate default roles and persists them to db
        """
        roles = {
            'admin': [
                Permissions.ADMIN,
                Permissions.ADD_SCHOOL,
                Permissions.ADD_TEACHER,
                Permissions.ADD_SCHOOL,
                Permissions.EDIT_SCHOOL,
                Permissions.REMOVE_SCHOOL,
                Permissions.REMOVE_TEACHER
            ],
            'teacher': [
                SchoolPermissions.ADD_COURSE,
                SchoolPermissions.EDIT_COURSE,
                SchoolPermissions.TAKE_COURSE,
                SchoolPermissions.TAKE_TEST,
                SchoolPermissions.DELETE_COURSE,
                SchoolPermissions.SEE_RESULTS
            ],
            'students': [
                SchoolPermissions.TAKE_COURSE,
                SchoolPermissions.TAKE_TEST,
                SchoolPermissions.SEE_RESULTS
            ],
            'generic': []
        }

        for role in roles:
            # check if role exists in db
            r = Role.query.filter_by(name=role).first()
            if not r:
                # if not in db create role
                r = Role(
                    name=role,
                    permissions=sum(roles[role])
                )
                db.session.add(r)
        
        # commit and close session
        try:
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()
        finally:
            db.session.close()


    @classmethod
    def get_role_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
