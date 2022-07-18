import pytest
from flask.testing import FlaskClient


@pytest.mark.usefixtures("app")
class TestMedicationGet:
    def test_medication_empty_get_returns_array(self, client: FlaskClient) -> None:
        response = client.get("/dhos/v1/medication")
        assert response.status_code == 200
        assert response.json == []

    def test_return_all_medications(
        self, client: FlaskClient, med_uuid: str, med_uuid_2: str
    ) -> None:
        response = client.get(f"/dhos/v1/medication")
        assert response.status_code == 200
        assert response.json is not None
        assert len(response.json) == 2
        assert {med_uuid, med_uuid_2} == {m["uuid"] for m in response.json}

    @pytest.mark.parametrize(
        "tag,num_expected", [("nosuchtag", 0), ("tag1", 1), ("tag2", 1), ("gdm", 2)]
    )
    def test_return_filtered_medications(
        self,
        client: FlaskClient,
        med_uuid: str,
        med_uuid_2: str,
        med_with_tags_uuid: str,
        tag: str,
        num_expected: int,
    ) -> None:
        response = client.get(f"/dhos/v1/medication?tag={tag}")
        assert response.status_code == 200
        assert response.json is not None
        assert len(response.json) == num_expected

    def test_return_one_medication_with_correct_id(
        self, client: FlaskClient, med_uuid: str
    ) -> None:
        response = client.get(f"/dhos/v1/medication/{med_uuid}")
        assert response.status_code == 200
        assert response.json is not None
        assert response.json["uuid"] == med_uuid

    def test_medication_invalid_get(self, client: FlaskClient) -> None:
        response = client.get(f"/dhos/v1/medication/not_real")
        assert response == 404

    def test_medication_get_no_uuid(self, client: FlaskClient) -> None:
        response = client.get(f"/dhos/v1/medication/")
        assert response == 404
