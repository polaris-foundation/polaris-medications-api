"""empty message

Revision ID: 4a27def86d11
Revises: 1e87def86d02
Create Date: 2020-08-17 08:47:13.656095

"""
from alembic import op

medications = [
    {
        "name": "Apidra",
        "sct_code": "9211101000001108",
        "unit": "units",
        "uuid": "842706c5-a4f4-453e-9e12-bf1ef2602820"
    }
]


# revision identifiers, used by Alembic.
revision = '4a27def86d11'
down_revision = '1e87def86d02'
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

