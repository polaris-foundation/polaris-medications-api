"""GDM-4142 - Add new medication: Lyumjev

Revision ID: f60fe1058f7b
Revises: 01849b3814ec
Create Date: 2021-02-04 10:26:49.477589

"""
import json
from typing import Dict

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "f60fe1058f7b"
down_revision = "01849b3814ec"
branch_labels = None
depends_on = None


lyumjev: Dict = {
    "uuid": "c90bb151-dff8-4995-ae43-f60fe1058f7b",
    "name": "Lyumjev",
    "sct_code": "227391000001107",
    "tags": json.dumps(
        ["gdm-uk-default", "gdm-us-default", "dbm-uk-default", "dbm-us-default"]
    ),
    "unit": "unit",
    "created": "2021-10-14T13:00:00.000Z",
    "modified": "2021-10-14T13:00:00.000Z",
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
    conn.execute(medication_table.insert(), lyumjev)


def downgrade():
    conn = op.get_bind()

    q = "DELETE FROM medication WHERE uuid = :uuid;"

    conn.execute(sa.text(q), uuid=lyumjev["uuid"])
