"""empty message

Revision ID: 04130dce5db6
Revises: b33d9b716926
Create Date: 2023-09-20 03:53:51.575049

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '04130dce5db6'
down_revision = 'b33d9b716926'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('school', schema=None) as batch_op:
        batch_op.add_column(sa.Column('school_slug', sa.String(length=10), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('school', schema=None) as batch_op:
        batch_op.drop_column('school_slug')

    # ### end Alembic commands ###
