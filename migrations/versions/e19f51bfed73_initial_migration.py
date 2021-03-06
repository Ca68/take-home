"""Initial migration.

Revision ID: e19f51bfed73
Revises: 
Create Date: 2021-08-12 21:04:13.767229

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e19f51bfed73'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('trip_id', sa.Integer(), nullable=False),
    sa.Column('starttime', sa.DateTime(), nullable=True),
    sa.Column('stoptime', sa.DateTime(), nullable=True),
    sa.Column('bikeid', sa.Integer(), nullable=True),
    sa.Column('from_station_id', sa.Integer(), nullable=True),
    sa.Column('from_station_name', sa.String(), nullable=True),
    sa.Column('to_station_id', sa.Integer(), nullable=True),
    sa.Column('to_station_name', sa.String(), nullable=True),
    sa.Column('usertype', sa.String(), nullable=True),
    sa.Column('gender', sa.String(), nullable=True),
    sa.Column('birthday', sa.DateTime(), nullable=True),
    sa.Column('trip_duration', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('trip_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
