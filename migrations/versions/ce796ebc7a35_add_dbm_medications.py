"""add dbm medications

Revision ID: ce796ebc7a35
Revises: 9e70d9e890d8
Create Date: 2020-12-15 12:43:19.848276

"""
import json
from datetime import datetime as dt
from typing import Dict, List

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "ce796ebc7a35"
down_revision = "9e70d9e890d8"
branch_labels = None
depends_on = None

new_medications: List[Dict] = [
    {
        "created": "2020-12-17T17:30:00.000Z",
        "modified": "2020-12-17T17:30:00.000Z",
        "name": "Toujeo",
        "sct_code": "12471501000001100",
        "tags": ["dbm-uk-default"],
        "unit": "units",
        "uuid": "df52fd5d-3114-4e35-bb44-9acb1ce9f9cd",
    },
    {
        "created": "2020-12-17T17:30:00.000Z",
        "modified": "2020-12-17T17:30:00.000Z",
        "name": "Linagliptin",
        "sct_code": "703667006",
        "tags": ["dbm-uk-default"],
        "unit": "mg",
        "uuid": "55d2a111-8f3f-4275-8146-c37e6e0ab0cd",
    },
    {
        "created": "2020-12-17T17:30:00.000Z",
        "modified": "2020-12-17T17:30:00.000Z",
        "name": "Sitagliptin",
        "sct_code": "424106006",
        "tags": ["dbm-uk-default"],
        "unit": "mg",
        "uuid": "a0a04a3e-a579-453e-877a-579fe36b56eb",
    },
    {
        "created": "2020-12-17T17:30:00.000Z",
        "modified": "2020-12-17T17:30:00.000Z",
        "name": "Metformin MR",
        "sct_code": "39113511000001101",
        "tags": ["dbm-uk-default"],
        "unit": "mg",
        "uuid": "1ec81ede-3397-4904-a3f7-8f051204ab93",
    },
    {
        "created": "2020-12-17T17:30:00.000Z",
        "modified": "2020-12-17T17:30:00.000Z",
        "name": "Gliclazide",
        "sct_code": "325238000",
        "tags": ["dbm-uk-default"],
        "unit": "mg",
        "uuid": "e43ec98f-90dc-4f4b-8aad-f8cb370fbd16",
    },
    {
        "created": "2020-12-17T17:30:00.000Z",
        "modified": "2020-12-17T17:30:00.000Z",
        "name": "Glipizide",
        "sct_code": "26124005",
        "tags": ["dbm-uk-default"],
        "unit": "mg",
        "uuid": "f1b2cf0a-6512-41b6-9e53-fa11ad56bb5e",
    },
    {
        "created": "2020-12-17T17:30:00.000Z",
        "modified": "2020-12-17T17:30:00.000Z",
        "name": "Repaginide",
        "sct_code": "109074004",
        "tags": ["dbm-uk-default"],
        "unit": "mg",
        "uuid": "2bc09f4d-d64f-4a8f-a429-96d43800cccd",
    },
    {
        "created": "2020-12-17T17:30:00.000Z",
        "modified": "2020-12-17T17:30:00.000Z",
        "name": "Nateglinide",
        "sct_code": "134604002",
        "tags": ["dbm-uk-default"],
        "unit": "mg",
        "uuid": "a4dc9015-8377-4d4a-bd40-06d7ad158c11",
    },
    {
        "created": "2020-12-17T17:30:00.000Z",
        "modified": "2020-12-17T17:30:00.000Z",
        "name": "Dapaglifozin",
        "sct_code": "703678003",
        "tags": ["dbm-uk-default"],
        "unit": "mg",
        "uuid": "f326bd82-a8db-4611-8a46-b326c5f00d25",
    },
    {
        "created": "2020-12-17T17:30:00.000Z",
        "modified": "2020-12-17T17:30:00.000Z",
        "name": "Empagliflozin",
        "sct_code": "703895009",
        "tags": ["dbm-uk-default"],
        "unit": "mg",
        "uuid": "1afd4b28-596c-4930-980f-de126460ba0a",
    },
    {
        "created": "2020-12-17T17:30:00.000Z",
        "modified": "2020-12-17T17:30:00.000Z",
        "name": "Canagliflozin",
        "sct_code": "703681008",
        "tags": ["dbm-uk-default"],
        "unit": "mg",
        "uuid": "450c9a8b-d438-4893-9f01-856bd952560d",
    },
    {
        "created": "2020-12-17T17:30:00.000Z",
        "modified": "2020-12-17T17:30:00.000Z",
        "name": "Bydureon",
        "sct_code": "10981401000001101",
        "tags": ["dbm-uk-default"],
        "unit": "mg",
        "uuid": "5e500cd5-5358-4f27-b4b9-5d1bdd9ac30e",
    },
    {
        "created": "2020-12-17T17:30:00.000Z",
        "modified": "2020-12-17T17:30:00.000Z",
        "name": "Byetta",
        "sct_code": "9228901000001108",
        "tags": ["dbm-uk-default"],
        "unit": "mg",
        "uuid": "a9cd170e-497b-40ce-a1c4-23585c512ab7",
    },
    {
        "created": "2020-12-17T17:30:00.000Z",
        "modified": "2020-12-17T17:30:00.000Z",
        "name": "Liraglutide",
        "sct_code": "444907006",
        "tags": ["dbm-uk-default"],
        "unit": "mg",
        "uuid": "69127895-32de-415b-b7b6-1b6ca08b77ed",
    },
    {
        "created": "2020-12-17T17:30:00.000Z",
        "modified": "2020-12-17T17:30:00.000Z",
        "name": "Dulaglutide",
        "sct_code": "714081009",
        "tags": ["dbm-uk-default"],
        "unit": "mg",
        "uuid": "32b6ea55-f055-4d61-a7e9-8c65c4f6104a",
    },
    {
        "created": "2020-12-17T17:30:00.000Z",
        "modified": "2020-12-17T17:30:00.000Z",
        "name": "Semaglutide",
        "sct_code": "36491911000001102",
        "tags": ["dbm-uk-default"],
        "unit": "mg",
        "uuid": "fb34cdb0-b057-4a61-8a98-6e5b815d75bf",
    },
]


def upgrade():
    medication_table = sa.table(
        "medication",
        sa.Column("uuid"),
        sa.Column("created"),
        sa.Column("modified"),
        sa.Column("sct_code"),
        sa.Column("name"),
        sa.Column("unit"),
        sa.Column("tags"),
    )
    op.bulk_insert(
        medication_table,
        [
            {
                "uuid": m["uuid"],
                "created": dt.fromisoformat(m["created"].replace("Z", "+00:00")),
                "modified": dt.fromisoformat(m["modified"].replace("Z", "+00:00")),
                "sct_code": m["sct_code"],
                "name": m["name"],
                "unit": m["unit"],
                "tags": json.dumps(m["tags"]),
            }
            for m in new_medications
        ],
    )


def downgrade():
    new_med_uuids: List[str] = [m["uuid"] for m in new_medications]
    op.get_bind().execute(
        sa.text("DELETE FROM medication WHERE uuid in :uuids").bindparams(
            sa.bindparam("uuids", value=new_med_uuids, expanding=True)
        )
    )
