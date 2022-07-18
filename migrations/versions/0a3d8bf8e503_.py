"""empty message

Revision ID: 0a3d8bf8e503
Revises: 4a27def86d11
Create Date: 2020-10-02 16:06:47.338758

"""
from alembic import op

medications = [
    {
        "name": "Semglee",
        "sct_code": "1327740100000110",
        "unit": "units",
        "uuid": "878fd365-235a-4db0-a610-13115ce99a21",
    },
    {
        "name": "Insulin Lispro Sanof",
        "sct_code": "35776411000001102",
        "unit": "units",
        "uuid": "ed77a4b7-3dc4-4546-a68b-77bc06764ecd",
    },
    {
        "name": "Glibenclamide",
        "sct_code": "80870001",
        "unit": "mg",
        "uuid": "367509fd-2fb6-44fe-9330-c9a9f0157aaf",
    },
    {
        "name": "Abasaglar",
        "sct_code": "12608101000001108",
        "unit": "ml",
        "uuid": "81549012-0753-4262-97b4-62b2bb17dc26",
    },
]

# revision identifiers, used by Alembic.
revision = "0a3d8bf8e503"
down_revision = "4a27def86d11"
branch_labels = None
depends_on = None


def upgrade():
    connection = op.get_bind()

    insert_query = """INSERT INTO medication (name, sct_code, unit, uuid, created, modified) 
    VALUES (%s, %s, %s, %s, NOW(), NOW())"""

    for medication in medications:

        params = (
            medication["name"],
            medication["sct_code"],
            medication["unit"],
            medication["uuid"],
        )

        connection.execute(insert_query, params)


def downgrade():
    connection = op.get_bind()

    delete_query = "DELETE FROM medication where uuid = %s"

    for medication in medications:

        params = medication["uuid"]

        connection.execute(delete_query, params)
