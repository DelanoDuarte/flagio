"""empty message

Revision ID: 93dc24d57ae5
Revises: a07d3ec815c5
Create Date: 2023-10-22 22:09:19.995871

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '93dc24d57ae5'
down_revision = 'a07d3ec815c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    #op.drop_table('environment_flags')
    # ### end Alembic commands ###
    pass


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('environment_flags',
    sa.Column('flag_id', sa.TEXT(length=36), nullable=True),
    sa.Column('environment_id', sa.TEXT(length=36), nullable=True),
    sa.ForeignKeyConstraint(['environment_id'], ['environment.id'], ),
    sa.ForeignKeyConstraint(['flag_id'], ['flag.id'], )
    )
    # ### end Alembic commands ###