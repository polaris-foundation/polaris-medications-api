"""Add Admelog

Revision ID: f04a82f653b1
Revises: af0e61a318e4
Create Date: 2022-03-07 14:49:28.243455

"""
import json
from typing import Dict

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "f04a82f653b1"
down_revision = "af0e61a318e4"
branch_labels = None
depends_on = None

admelog: Dict = {
    "uuid": "cda6ca7d-6d64-4a6e-a5d2-c7e045f92f5c",
    "name": "Admelog",
    "sct_code": "155181000001100",
    "tags": json.dumps(["gdm-uk-default", "dbm-uk-default"]),
    "unit": "units",
    "created": "2022-03-07T13:00:00.000Z",
    "modified": "2022-03-07T13:00:00.000Z",
}


def upgrade():
    print("Adding Admelog")
    conn = op.get_bind()
    medication_table = sa.table(
        "medication",
        sa.Column("uuid"),
        sa.Column("name"),
        sa.Column("sct_code"),
        sa.Column("tags"),
        sa.Column("unit"),
        sa.Column("created"),
        sa.Column("modified"),
    )
    conn.execute(medication_table.insert(), admelog)


def downgrade():
    print("Removing Admelog")

    conn = op.get_bind()

    q = "DELETE FROM medication WHERE uuid = :uuid;"

    conn.execute(sa.text(q), uuid=admelog["uuid"])
