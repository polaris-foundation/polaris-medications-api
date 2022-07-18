"""empty message

Revision ID: 5436fd4dfc35
Revises: 955292e25fbc
Create Date: 2018-01-29 17:11:41.763642

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5436fd4dfc35'
down_revision = 'c335803fc6c2'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_index('only_one_active_medication', table_name='medication')
    op.create_index('only_one_active_medication_ci',
                    'medication', [sa.text('lower(name)')],
                    postgresql_where=(sa.text('deleted IS NULL')),
                    unique=True)


def downgrade():
    op.create_index('only_one_active_medication', 'medication', [
                    'name'],
                    unique=True, postgresql_where=sa.text('deleted IS NULL'))
    op.drop_index('only_one_active_medication_ci')
