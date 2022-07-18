from pathlib import Path
from typing import Dict, List

import yaml
from behave import step, then
from behave.runner import Context
from clients import medication_client
from helpers import medication as medication_helper
from requests import Response, codes


@step("a new medication is created")
def create_new_medication(context: Context) -> None:
    new_medication = medication_helper.get_body()
    response: Response = medication_client.create_medication(body=new_medication)
    response.raise_for_status()
    response_json: dict = response.json()
    assert "uuid" in response_json
    context.medication_uuid = response_json["uuid"]
    context.medication_uuids += [response_json["uuid"]]
    context.medication_body = response_json


@step("the medication {can_or_can_not} be retrieved by its uuid")
def get_medication_by_uuid(context: Context, can_or_can_not: str) -> None:
    response: Response = medication_client.get_medication(uuid=context.medication_uuid)

    if can_or_can_not == "can":
        response.raise_for_status()
        context.api_medication_body = response.json()
    else:
        assert response.status_code == codes.not_found


@step("the medication {can_or_can_not} be seen in the medication list")
def assert_medication_in_all_medications(context: Context, can_or_can_not: str) -> None:
    response: Response = medication_client.get_all_medications()
    response.raise_for_status()
    all_ids: list = [q["uuid"] for q in response.json()]

    if can_or_can_not == "can":
        assert context.medication_uuid in all_ids
    else:
        assert context.medication_uuid not in all_ids


@step("the medication matches that previously created")
def assert_medication_body(context: Context) -> None:
    for attribute in ["name", "sct_code", "unit", "tags"]:
        assert (
            context.medication_body[attribute] == context.api_medication_body[attribute]
        )


@step("the medication is updated")
def update_medication(context: Context) -> None:
    body: dict = medication_helper.get_body()
    context.medication_body = body

    response: Response = medication_client.update_medication(
        uuid=context.medication_uuid, body=body
    )
    response.raise_for_status()
    context.updated_medication_body = response.json()


@step("the updated medication is persisted")
def assert_updated_body(context: Context) -> None:
    for attribute in ["name", "sct_code", "unit", "tags"]:
        assert (
            context.medication_body[attribute]
            == context.updated_medication_body[attribute]
        )


@step("the medication is deleted")
def delete_medication(context: Context) -> None:
    response: Response = medication_client.delete_medication(
        uuid=context.medication_uuid
    )
    response.raise_for_status()


@then("the medication can be retrieved by its tags")
def get_medication_by_tags(context: Context) -> None:
    medication_tags: List[str] = context.medication_body["tags"]
    medication_uuid: str = context.medication_body["uuid"]
    for tag in medication_tags:
        response = medication_client.get_all_medications(tag=tag)
        response.raise_for_status()
        assert medication_uuid in [m["uuid"] for m in response.json()]


@then("there are the expected {locale} medications for {product}")
def check_static_medications_by_locale(
    context: Context, locale: str, product: str
) -> None:
    tag = f"{product.lower()}-{locale.lower()}"
    static_meds_file = (
        Path(__file__).parent.parent / "fixtures" / "expected_static_meds.yaml"
    )
    static_medications = yaml.load(static_meds_file.read_text(), Loader=yaml.FullLoader)
    expected_meds: List[Dict] = [m for m in static_medications if tag in m["tags"]]
    response: Response = medication_client.get_all_medications(
        tag=tag,
    )
    response.raise_for_status()
    assert sorted(response.json(), key=lambda x: x["name"]) == sorted(
        expected_meds, key=lambda x: x["name"]
    )
    assert len(response.json()) > 0
