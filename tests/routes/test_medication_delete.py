import pytest
from flask.testing import FlaskClient


@pytest.mark.usefixtures("app")
class TestMedicationDeleteTest:
    def test_delete_medication_with_correct_id(
        self, client: FlaskClient, med_uuid: str
    ) -> None:
        response = client.delete(f"/dhos/v1/medication/{med_uuid}")
        assert response.status_code == 200
        assert response.json is not None
        assert response.json["deleted"] is not None

    def test_medication_invalid_delete(self, client: FlaskClient) -> None:
        response = client.delete("/dhos/v1/medication/not_real")
        assert response.status_code == 404

    def test_medication_delete_no_uuid(self, client: FlaskClient) -> None:
        response = client.delete("/dhos/v1/medication/")
        assert response.status_code == 404
