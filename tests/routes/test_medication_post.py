import pytest
from flask.testing import FlaskClient


@pytest.mark.usefixtures("app")
class TestMedicationPost:
    def test_medication_post_no_json(self, client: FlaskClient) -> None:
        response = client.post("/dhos/v1/medication")
        assert response.status_code == 400

    def test_medication_post_invalid_json(self, client: FlaskClient) -> None:
        response = client.post(
            "/dhos/v1/medication",
            json={"invalid": True},
        )
        assert response == 400

    def test_medication_post_without_name(self, client: FlaskClient) -> None:
        response = client.post(
            "/dhos/v1/medication",
            json={"unit": "mmol"},
        )
        assert response == 400

    def test_medication_post_without_unit(self, client: FlaskClient) -> None:
        response = client.post(
            "/dhos/v1/medication",
            json={"name": "Insulin"},
        )
        assert response == 400

    def test_medication_post_with_valid_data(self, client: FlaskClient) -> None:
        payload = {
            "unit": "units",
            "name": "Insulin",
            "sct_code": "1234",
            "tags": ["gdm"],
        }
        response = client.post(
            "/dhos/v1/medication",
            json=payload,
        )
        assert response == 200
        assert response.json is not None
        assert response.json["name"] == "Insulin"

    def test_two_medication_post_with_valid_data_and_existing_tag(
        self, client: FlaskClient
    ) -> None:
        payload1 = {
            "unit": "units",
            "name": "Insulin",
            "sct_code": "1234",
            "tags": ["gdm"],
        }
        payload2 = {
            "unit": "units",
            "name": "InsulinPlus",
            "sct_code": "1234",
            "tags": ["gdm"],
        }
        response1 = client.post(
            "/dhos/v1/medication",
            json=payload1,
        )
        response2 = client.post(
            "/dhos/v1/medication",
            json=payload2,
        )
        assert response1 == 200
        assert response2 == 200
        assert response1.json is not None
        assert response2.json is not None
        assert response1.json["name"] == "Insulin"
        assert response2.json["name"] == "InsulinPlus"

    def test_two_medication_post_with_invalid_data_and_existing_tag(
        self, client: FlaskClient
    ) -> None:
        payload = {
            "unit": "units",
            "name": "Insulin",
            "sct_code": "1234",
            "tags": ["gdm"],
        }
        response1 = client.post(
            "/dhos/v1/medication",
            json=payload,
        )
        response2 = client.post(
            "/dhos/v1/medication",
            json=payload,
        )
        assert response1 == 200
        assert response2 == 409

    def test_two_medication_post_duplicate(self, client: FlaskClient) -> None:
        payload1 = {
            "unit": "units",
            "name": "Insulin",
            "sct_code": "1234",
            "tags": ["gdm"],
        }
        payload2 = {
            "unit": "units",
            "name": "insulin",
            "sct_code": "1234",
            "tags": ["gdm"],
        }
        response1 = client.post(
            "/dhos/v1/medication",
            json=payload1,
        )
        response2 = client.post(
            "/dhos/v1/medication",
            json=payload2,
        )
        assert response1 == 200
        assert response2 == 409
