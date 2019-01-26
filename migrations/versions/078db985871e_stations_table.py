"""stations table

Revision ID: 078db985871e
Revises: 5f6affaa687f
Create Date: 2019-01-26 12:43:39.241296

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '078db985871e'
down_revision = '5f6affaa687f'
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
    sa.Column('id', sa.Integer(), nullable=False),
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
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_ride_start_time'), 'ride', ['start_time'], unique=False)
    op.drop_index('ix_rides_start_time', table_name='rides')
    op.drop_table('rides')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rides',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('start_time', sa.DATETIME(), nullable=True),
    sa.Column('end_time', sa.DATETIME(), nullable=True),
    sa.Column('bike_id', sa.INTEGER(), nullable=True),
    sa.Column('trip_duration', sa.FLOAT(), nullable=True),
    sa.Column('from_station_id', sa.INTEGER(), nullable=True),
    sa.Column('to_station_id', sa.INTEGER(), nullable=True),
    sa.Column('user_type', sa.VARCHAR(length=50), nullable=True),
    sa.Column('gender', sa.VARCHAR(length=20), nullable=True),
    sa.Column('birth_year', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_rides_start_time', 'rides', ['start_time'], unique=False)
    op.drop_index(op.f('ix_ride_start_time'), table_name='ride')
    op.drop_table('ride')
    op.drop_table('station')
    # ### end Alembic commands ###
