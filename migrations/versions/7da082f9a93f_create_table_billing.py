"""create table billing

Revision ID: 7da082f9a93f
Revises: c8b6dfdf94ca
Create Date: 2019-07-21 19:46:51.977143

"""
from datetime import datetime

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '7da082f9a93f'
down_revision = 'c8b6dfdf94ca'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('billing',
                    sa.Column('id',
                              sa.Interval,
                              primary_key=True),
                    sa.Column('title',
                              sa.String(250),
                              nullable=False),
                    sa.Column('description',
                              sa.Text,
                              nullable=False),
                    sa.Column('value',
                              sa.Numeric(10, 2),
                              nullable=False),
                    sa.Column('work_date',
                              sa.DateTime,
                              nullable=False,
                              default=datetime.utcnow),
                    sa.Column('receive_date',
                              sa.DateTime,
                              nullable=True,
                              default=None),
                    sa.Column('received',
                              sa.Boolean,
                              nullable=False,
                              default=False),
                    sa.Column('user_id',
                              sa.Integer,
                              sa.ForeignKey('user.id'),
                              nullable=False))


def downgrade():
    op.drop_table('billing')
