"""PLAT-958 - Add new medication: Trurapi

Revision ID: af0e61a318e4
Revises: 8aef231c7943
Create Date: 2021-11-24 13:00:00.000000

"""
import json
from typing import Dict

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "af0e61a318e4"
down_revision = "8aef231c7943"
branch_labels = None
depends_on = None


trurapi: Dict = {
    "uuid": "af0e61a3-18e4-4547-9e69-3a7d1f219c54",
    "name": "Trurapi",
    "sct_code": "94371000001104",
    "tags": json.dumps(
        ["gdm-uk-default", "gdm-us-default", "dbm-uk-default", "dbm-us-default"]
    ),
    "unit": "unit",
    "created": "2021-11-24T13:00:00.000Z",
    "modified": "2021-11-24T13:00:00.000Z",
}


def upgrade():
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
    conn.execute(medication_table.insert(), trurapi)


def downgrade():
    conn = op.get_bind()

    q = "DELETE FROM medication WHERE uuid = :uuid;"

    conn.execute(sa.text(q), uuid=trurapi["uuid"])
