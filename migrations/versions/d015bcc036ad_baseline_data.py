"""baseline data

Revision ID: d015bcc036ad
Revises: 3bdf0fdc4028
Create Date: 2018-04-10 15:00:32.691361

"""
from alembic import op

medications = [
    {
        "name": "Humalog Mix25",
        "sct_code": "9489901000001108",
        "unit": "units",
        "uuid": "5350a08a-070f-48e4-b156-3d6f7ab48efa"
    },
    {
        "name": "Humalog Mix50",
        "sct_code": "9512801000001102",
        "unit": "units",
        "uuid": "ed870a96-23df-4177-bb0c-575db80caf6f"
    },
    {
        "name": "Humulin M3",
        "sct_code": "9530701000001100",
        "unit": "units",
        "uuid": "0a8bb2af-e314-4180-8ac4-fa6a9d7e512b"
    },
    {
        "name": "Novomix 30",
        "sct_code": "9483001000001106",
        "unit": "units",
        "uuid": "f3cf91ed-a04e-48d2-9c8e-02b3492ef23c"
    },
    {
        "name": "Humulin I",
        "sct_code": "9450101000001108",
        "unit": "units",
        "uuid": "76c88ab6-f38a-4a40-9078-1da50d0b5403"
    },
    {
        "name": "Insulatard",
        "sct_code": "9484401000001103",
        "unit": "units",
        "uuid": "437b20da-03b5-496e-91fa-727d1a47531a"
    },
    {
        "name": "Lantus",
        "sct_code": "12759201000001105",
        "unit": "units",
        "uuid": "23b9d0a3-2982-4479-9b42-29d703058579"
    },
    {
        "name": "Levemir",
        "sct_code": "9520901000001101",
        "unit": "units",
        "uuid": "aa5d2790-c8d9-4858-a2a2-ffda64c831d6"
    },
    {
        "name": "Actrapid",
        "sct_code": "9196601000001105",
        "unit": "units",
        "uuid": "c28945e5-198e-4ac5-b6ef-813458d1ab9b"
    },
    {
        "name": "Humulin S",
        "sct_code": "9530801000001109",
        "unit": "units",
        "uuid": "73bb73d9-e892-4fe7-9cd5-d6730899cf6f"
    },
    {
        "name": "Humalog",
        "sct_code": "9538601000001108",
        "unit": "units",
        "uuid": "1fdf2331-70f8-483b-867a-9e764e9e91ff"
    },
    {
        "name": "NovoRapid",
        "sct_code": "9518101000001108",
        "unit": "units",
        "uuid": "69d77158-4f36-4a1e-90e5-f250ea33d4b9"
    },
    {
        "name": "Metformin",
        "sct_code": "109081006",
        "unit": "mg",
        "uuid": "0ee36cf8-945b-4b44-848c-2c73e614bb56"
    }
]

# revision identifiers, used by Alembic.
revision = 'd015bcc036ad'
down_revision = '3bdf0fdc4028'
branch_labels = None
depends_on = None


def upgrade():
    connection = op.get_bind()
    for medication in medications:
        insert = "insert into medication " + \
            "(name, sct_code, unit, uuid, created, modified) " + \
            "VALUES (" + \
            "'" + medication["name"] + "', " + \
            "'" + medication["sct_code"] + "', " + \
            "'" + medication["unit"] + "', " + \
            "'" + medication["uuid"] + "', " + \
            " NOW(), " + \
            " NOW())"
        connection.execute(insert)


def downgrade():
    connection = op.get_bind()
    for medication in medications:
        delete = "DELETE FROM medication where uuid = '" + \
            medication["uuid"] + "'"
        connection.execute(delete)
