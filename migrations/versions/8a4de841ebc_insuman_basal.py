"""GDM-4142 - Add new medication: Lyumjev

Revision ID: 8a4de841ebc
Revises: f60fe1058f7b
Create Date: 2021-02-04 10:26:49.477589

"""
import json
from typing import Dict

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "8a4de841ebc"
down_revision = "f60fe1058f7b"
branch_labels = None
depends_on = None


insuman_basal: Dict = {
    "uuid": "8a4de841-ebcd-4652-9c56-6c146aa574ec",
    "name": "Insuman Basal",
    "sct_code": "9484501000001104",
    "tags": json.dumps(
        ["gdm-uk-default", "gdm-us-default", "dbm-uk-default", "dbm-us-default"]
    ),
    "unit": "unit",
    "created": "2021-11-04T13:00:00.000Z",
    "modified": "2021-11-04T13:00:00.000Z",
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
    conn.execute(medication_table.insert(), insuman_basal)


def downgrade():
    conn = op.get_bind()

    q = "DELETE FROM medication WHERE uuid = :uuid;"

    conn.execute(sa.text(q), uuid=insuman_basal["uuid"])
