from main import db
from models.base import IdMixin


class Permissions:
    ADD_COURSE = 2
    EDIT_COURSE = 4
    DELETE_COURSE = 8
    TAKE_COURSE = 16
    TAKE_ASSESSMENT = 32
    ADMIN = 64


class User(db.Model, IdMixin):
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    email = db.Column(db.String(50))
    password = db.Column(db.String(300))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))


class Student(db.Model, IdMixin):
    student_id = db.Column(db.String, nullable=False, unique=True)
    gpa = db.Column(db.Integer, nullable=False)

    def update_gpa(self):
        pass

    def fetch_results(self):
        pass


class Teacher(db.Model, IdMixin):
    teacher_id = db.Column(db.String, nullable=False, unique=True)
    courses = db.relationship('Course', backref='teacher')



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
            'admin': [Permissions.ADMIN],
            'teacher': [
                Permissions.ADD_COURSE,
                Permissions.EDIT_COURSE,
                Permissions.TAKE_COURSE,
                Permissions.TAKE_ASSESSMENT,
                Permissions.DELETE_COURSE
            ],
            'students': [Permissions.TAKE_COURSE,
                Permissions.TAKE_ASSESSMENT],
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
