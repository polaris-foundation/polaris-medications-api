"""empty message

Revision ID: 5992778efb39
Revises: 3bdf0fdc4028
Create Date: 2018-04-16 18:17:19.700067

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5992778efb39'
down_revision = 'd015bcc036ad'
branch_labels = None
depends_on = None


def upgrade():

    op.add_column('medication', sa.Column('created_by_', sa.String(), nullable=False, server_default='sys'))
    op.add_column('medication', sa.Column('modified_by_', sa.String(), nullable=False, server_default='sys'))
    op.add_column('tag', sa.Column('created_by_', sa.String(), nullable=False, server_default='sys'))
    op.add_column('tag', sa.Column('modified_by_', sa.String(), nullable=False, server_default='sys'))


def downgrade():

    op.drop_column('tag', 'modified_by_')
    op.drop_column('tag', 'created_by_')
    op.drop_column('medication', 'modified_by_')
    op.drop_column('medication', 'created_by_')
