"""adding to medications

Revision ID: a746b8ca1051
Revises: 5992778efb39
Create Date: 2018-08-29 15:44:42.414160

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a746b8ca1051'
down_revision = '5992778efb39'
branch_labels = None
depends_on = None


metformin_slow_release = {
    'name': 'Metformin Slow Release',
    'sct_code': '411533003',
    'unit': 'mg',
    'uuid': '9762c971-78a6-47f3-bf29-cbc7c3c68b42'
}


def upgrade():

    insert = "insert into medication " + \
             "(name, sct_code, unit, uuid, created, modified) " + \
             "VALUES (" + \
             "'" + metformin_slow_release["name"] + "', " + \
             "'" + metformin_slow_release["sct_code"] + "', " + \
             "'" + metformin_slow_release["unit"] + "', " + \
             "'" + metformin_slow_release["uuid"] + "', " + \
             " NOW(), " + \
             " NOW())"

    connection = op.get_bind()
    connection.execute(insert)


def downgrade():
    delete = f"DELETE FROM medication where " \
             f"uuid = '{metformin_slow_release['uuid']}'"

    connection = op.get_bind()
    connection.execute(delete)
