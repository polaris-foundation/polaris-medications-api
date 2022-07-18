import pytest
from flask.testing import FlaskClient


@pytest.mark.usefixtures("app")
class TestMedicationPatch:
    def test_medication_patch_no_json(self, client: FlaskClient) -> None:
        response = client.patch("/dhos/v1/medication/123")
        assert response.status_code == 400

    def test_medication_patch_unknown(self, client: FlaskClient) -> None:
        response = client.patch(
            "/dhos/v1/medication/123",
            json={"invalid": True},
        )
        assert response == 404

    def test_medication_patch_alter_medication_unit(
        self, client: FlaskClient, med_uuid: str
    ) -> None:
        response = client.patch(
            f"/dhos/v1/medication/{med_uuid}",
            json={"unit": "mmol"},
        )
        assert response.status_code == 200
        assert response.json is not None
        assert response.json["unit"] == "mmol"

    def test_medication_patch_remove_tag(
        self, client: FlaskClient, med_uuid: str
    ) -> None:
        response = client.patch(
            f"/dhos/v1/medication/{med_uuid}",
            json={"tags": []},
        )
        assert response.status_code == 200
        assert response.json is not None
        assert response.json["tags"] == []

    def test_medication_patch_empty_json(
        self, client: FlaskClient, med_uuid: str
    ) -> None:
        response = client.patch(
            f"/dhos/v1/medication/{med_uuid}",
            json={},
        )
        assert response.status_code == 400

    def test_medication_patch_alter_medication_name(
        self, client: FlaskClient, med_uuid: str
    ) -> None:
        response = client.patch(
            f"/dhos/v1/medication/{med_uuid}",
            json={"name": "InsulinPlus"},
        )
        assert response.status_code == 200
        assert response.json is not None
        assert response.json["name"] == "InsulinPlus"

    def test_medication_patch_alter_medication_to_existing_name(
        self, client: FlaskClient, med_uuid: str, med_uuid_2: str
    ) -> None:
        response = client.patch(
            f"/dhos/v1/medication/{med_uuid_2}",
            json={"name": "Insulin"},
        )
        assert response.status_code == 409

    def test_medication_patch_alter_medication_to_empty_name(
        self, client: FlaskClient, med_uuid: str
    ) -> None:
        response = client.patch(
            f"/dhos/v1/medication/{med_uuid}",
            json={"name": ""},
        )
        assert response.status_code == 400

    def test_medication_patch_alter_medication_to_empty_unit(
        self, client: FlaskClient, med_uuid: str
    ) -> None:
        response = client.patch(
            f"/dhos/v1/medication/{med_uuid}",
            json={"unit": ""},
        )
        assert response.status_code == 400

    def test_medication_patch_alter_medication_tags(
        self, client: FlaskClient, med_uuid: str
    ) -> None:
        response = client.patch(
            f"/dhos/v1/medication/{med_uuid}",
            json={"tags": ["gdm", "fishing"]},
        )
        assert response.status_code == 200
        assert response.json is not None
        assert len(response.json["tags"]) == 2
