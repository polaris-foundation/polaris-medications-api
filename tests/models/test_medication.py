from datetime import datetime

import pytest
from flask_batteries_included.sqldb import db

from dhos_medications_api.models.medication import Medication


@pytest.mark.usefixtures("app")
class TestMedication:
    def test_to_dict(self, med_uuid: str) -> None:
        medication = Medication.query.filter_by(uuid=med_uuid).first()
        med_dict = medication.to_dict()
        assert medication is not None
        assert len(med_dict) == 9
        assert med_dict["uuid"] == medication.uuid
        assert isinstance(med_dict["created"], datetime)
        assert isinstance(med_dict["modified"], datetime)
        assert isinstance(med_dict["name"], str)
        assert isinstance(med_dict["unit"], str)

    def test_created_gets_generated(self, med_uuid: str) -> None:
        medication = Medication.query.filter_by(uuid=med_uuid).first()
        assert medication is not None

    def test_deleted_gets_generated(self, med_uuid: str) -> None:
        medication = Medication.query.filter_by(uuid=med_uuid).first()
        medication.delete()
        db.session.add(medication)
        db.session.commit()
        result = Medication.query.filter_by(uuid=med_uuid).with_deleted().first()
        assert result.deleted is not None

    def test_medication_get(self, med_uuid: str) -> None:
        medication = Medication.query.get(med_uuid)
        assert medication is not None
