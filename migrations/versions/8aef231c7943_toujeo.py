"""GDM-4206 - Update medication: Toujeo

Revision ID: 8aef231c7943
Revises: 8a4de841ebc
Create Date: 2021-02-04 10:26:49.477589

"""

from alembic import op

# revision identifiers, used by Alembic.
revision = "8aef231c7943"
down_revision = "8a4de841ebc"
branch_labels = None
depends_on = None

toujeo_uuid = "df52fd5d-3114-4e35-bb44-9acb1ce9f9cd"


def upgrade():
    toujeo_tag: str = '["gdm-uk-default","gdm-us-default","dbm-uk-default"]'
    op.execute(f"UPDATE medication SET tags='{toujeo_tag}' WHERE uuid='{toujeo_uuid}'")


def downgrade():
    toujeo_tag: str = '["dbm-uk-default","dbm-us-default"]'
    op.execute(f"UPDATE medication SET tags='{toujeo_tag}' WHERE uuid='{toujeo_uuid}'")
