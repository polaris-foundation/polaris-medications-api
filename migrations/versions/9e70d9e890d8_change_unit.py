"""change unit

Revision ID: 9e70d9e890d8
Revises: fc4186614721
Create Date: 2020-11-30 14:49:28.243455

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = "9e70d9e890d8"
down_revision = "fc4186614721"
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        "UPDATE medication SET unit='units' WHERE uuid='81549012-0753-4262-97b4-62b2bb17dc26'"
    )


def downgrade():
    op.execute(
        "UPDATE medication SET unit='ml' WHERE uuid='81549012-0753-4262-97b4-62b2bb17dc26'"
    )
