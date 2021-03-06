"""initial db structures

Revision ID: 15db0de3cb67
Revises: 
Create Date: 2019-03-19 08:25:43.939373

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15db0de3cb67'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('station',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('station_name', sa.String(length=150), nullable=True),
    sa.Column('latitude', sa.Float(), nullable=True),
    sa.Column('longitude', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ride',
    sa.Column('trip_id', sa.Integer(), nullable=False),
    sa.Column('start_time', sa.DateTime(), nullable=True),
    sa.Column('end_time', sa.DateTime(), nullable=True),
    sa.Column('bike_id', sa.Integer(), nullable=True),
    sa.Column('trip_duration', sa.Float(), nullable=True),
    sa.Column('from_station_id', sa.Integer(), nullable=True),
    sa.Column('to_station_id', sa.Integer(), nullable=True),
    sa.Column('user_type', sa.String(length=50), nullable=True),
    sa.Column('gender', sa.String(length=20), nullable=True),
    sa.Column('birth_year', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['from_station_id'], ['station.id'], ),
    sa.ForeignKeyConstraint(['to_station_id'], ['station.id'], ),
    sa.PrimaryKeyConstraint('trip_id')
    )
    op.create_index(op.f('ix_ride_start_time'), 'ride', ['start_time'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_ride_start_time'), table_name='ride')
    op.drop_table('ride')
    op.drop_table('station')
    # ### end Alembic commands ###
