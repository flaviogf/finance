"""create table user

Revision ID: c8b6dfdf94ca
Revises: 
Create Date: 2019-07-21 12:00:17.325488

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'c8b6dfdf94ca'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('user',
                    sa.Column('id',
                              sa.Integer,
                              primary_key=True),
                    sa.Column('name',
                              sa.String(250),
                              nullable=False),
                    sa.Column('email',
                              sa.String(250),
                              nullable=False,
                              unique=True),
                    sa.Column('image',
                              sa.String(250),
                              nullable=False,
                              default='default.jpg'),
                    sa.Column('password',
                              sa.String(250),
                              nullable=False))


def downgrade():
    op.drop_table('user')
