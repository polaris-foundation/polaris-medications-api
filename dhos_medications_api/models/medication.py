from datetime import datetime
from typing import Dict

from flask_batteries_included.sqldb import ModelIdentifier, db

from dhos_medications_api.queries.softdelete import QueryWithSoftDelete


class Medication(ModelIdentifier, db.Model):
    query_class = QueryWithSoftDelete

    sct_code = db.Column(db.String, unique=False, nullable=False)
    name = db.Column(db.String, unique=False, nullable=False)
    unit = db.Column(db.String, unique=False, nullable=False)
    deleted = db.Column(db.DateTime, unique=False, nullable=True)
    tags = db.Column(db.JSON, unique=False, nullable=False)

    @staticmethod
    def schema() -> Dict:
        return {
            "optional": {"tags": list},
            "required": {"name": str, "unit": str, "sct_code": str},
            "updatable": {"name": str, "unit": str, "tags": list, "sct_code": str},
        }

    def to_dict(self) -> Dict:
        medication = {
            "name": self.name,
            "unit": self.unit,
            "sct_code": self.sct_code,
            "tags": self.tags,
        }

        if self.deleted is not None:
            medication["deleted"] = self.deleted

        return {**medication, **self.pack_identifier()}

    def delete(self) -> None:
        self.deleted = datetime.utcnow()
