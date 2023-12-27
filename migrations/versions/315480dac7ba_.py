"""empty message

Revision ID: 315480dac7ba
Revises: 
Create Date: 2023-12-24 14:31:56.701117

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '315480dac7ba'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cliente',
    sa.Column('id', sa.Integer, autoincrement=True, nullable=False),
    sa.Column('name', sa.String(100), nullable=False),
    sa.Column('cell_contact', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('street_address', sa.String(length=100), nullable=False),
    sa.Column('city_address', sa.String(length=100), nullable=False),
    sa.Column('state_address', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cell_contact'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cliente')
    # ### end Alembic commands ###
