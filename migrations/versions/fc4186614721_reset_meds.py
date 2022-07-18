"""Reset meds for new multitenanted instance

Revision ID: fc4186614721
Revises: ef563dfdc6bc
Create Date: 2020-10-28 16:54:06.916581

"""
import json
from datetime import datetime as dt
from pathlib import Path
from typing import Dict, List

import sqlalchemy as sa
import yaml
from alembic import op

# revision identifiers, used by Alembic.
revision = "fc4186614721"
down_revision = "ef563dfdc6bc"
branch_labels = None
depends_on = None


def upgrade():
    meds_file: Path = Path(__file__).parent.parent / "medications_20201028.yaml"
    medications: List[Dict] = yaml.load(meds_file.read_text(), Loader=yaml.FullLoader)
    op.execute("DELETE FROM medication")
    op.execute("DROP INDEX IF EXISTS only_one_active_medication")
    op.execute("DROP INDEX IF EXISTS only_one_active_medication_ci")

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
            for m in medications
        ],
    )


def downgrade():
    """No value in having a downgrade."""
