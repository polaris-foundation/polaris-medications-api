"""rename medications

Revision ID: 07b1d3819711
Revises: ce796ebc7a35
Create Date: 2020-12-18 14:40:00.687535

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = "07b1d3819711"
down_revision = "ce796ebc7a35"
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        "UPDATE medication SET name='Repaglinide' WHERE uuid='2bc09f4d-d64f-4a8f-a429-96d43800cccd'"
    )
    op.execute(
        "UPDATE medication SET name='Dapagliflozin' WHERE uuid='f326bd82-a8db-4611-8a46-b326c5f00d25'"
    )


def downgrade():
    op.execute(
        "UPDATE medication SET name='Repaginide' WHERE uuid='2bc09f4d-d64f-4a8f-a429-96d43800cccd'"
    )
    op.execute(
        "UPDATE medication SET name='Dapaglifozin' WHERE uuid='f326bd82-a8db-4611-8a46-b326c5f00d25'"
    )
