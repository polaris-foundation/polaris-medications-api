"""empty message

Revision ID: 1e87def86d02
Revises: a746b8ca1051
Create Date: 2018-10-04 11:25:56.496095

"""
from alembic import op

medications = [
    {
        "name": "Fiasp",
        "sct_code": "13017301000001108",
        "unit": "units",
        "uuid": "01a31b69-bff8-4124-bbcc-14587c6c3a2b",
    },
    {
        "name": "Tresiba",
        "sct_code": "11706801000001105",
        "unit": "units",
        "uuid": "e2521f7a-b6ab-4c6d-8f0c-916e405bcb7b",
    },
]


# revision identifiers, used by Alembic.
revision = "1e87def86d02"
down_revision = "a746b8ca1051"
branch_labels = None
depends_on = None


def upgrade():
    connection = op.get_bind()
    for medication in medications:
        insert = (
            "insert into medication "
            + "(name, sct_code, unit, uuid, created, modified) "
            + "VALUES ("
            + "'"
            + medication["name"]
            + "', "
            + "'"
            + medication["sct_code"]
            + "', "
            + "'"
            + medication["unit"]
            + "', "
            + "'"
            + medication["uuid"]
            + "', "
            + " NOW(), "
            + " NOW())"
        )
        connection.execute(insert)


def downgrade():
    connection = op.get_bind()
    for medication in medications:
        delete = "DELETE FROM medication where uuid = '" + medication["uuid"] + "'"
        connection.execute(delete)
