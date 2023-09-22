from main import ma
from models.school import School


class SchoolSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = School
        load_instance = True

        dump_only = (
            'code',
            'user_id',
            'school_slug',
        )

