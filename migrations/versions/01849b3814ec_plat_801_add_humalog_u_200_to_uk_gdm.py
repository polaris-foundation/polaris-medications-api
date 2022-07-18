"""PLAT-801 Add Humalog U-200 to UK GDm

Revision ID: 01849b3814ec
Revises: 07b1d3819711
Create Date: 2021-02-04 10:26:49.477589

"""
import json
from typing import Dict

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01849b3814ec'
down_revision = '07b1d3819711'
branch_labels = None
depends_on = None


humalog: Dict = {
    "uuid": "4712ec21-e972-466b-a1d7-3e396ce137e3",
    "name": "Humalog U-200",
    "sct_code": "28989711000001106",
    "tags": json.dumps(["gdm-uk-default"]),
    "unit": "units/mL",
    "created": "2021-02-04T13:00:00.000Z",
    "modified": "2021-02-04T13:00:00.000Z"
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
        sa.Column("modified")
    )
    conn.execute(medication_table.insert(), humalog)


def downgrade():
    conn = op.get_bind()

    q = "DELETE FROM medication WHERE uuid = :uuid;"

    conn.execute(sa.text(q), uuid=humalog["uuid"])
