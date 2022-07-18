from typing import Generator

import pytest
from flask import Flask
from flask_batteries_included.sqldb import db, generate_uuid
from sqlalchemy.exc import InvalidRequestError

from dhos_medications_api.models.medication import Medication


@pytest.fixture()
def app() -> Flask:
    """Fixture that creates app for testing"""
    import dhos_medications_api.app

    return dhos_medications_api.app.create_app(
        testing=True, use_pgsql=False, use_sqlite=True
    )


@pytest.fixture
def app_context(app: Flask) -> Generator[None, None, None]:
    with app.app_context():
        yield


@pytest.fixture
def med_uuid() -> Generator[str, None, None]:
    medication = Medication(
        uuid=generate_uuid(), name="Insulin", sct_code="1234", unit="mmol", tags=["gdm"]
    )
    db.session.add(medication)
    db.session.commit()

    yield medication.uuid

    try:
        db.session.delete(medication)
    except InvalidRequestError:
        pass
    db.session.commit()


@pytest.fixture
def med_uuid_2() -> Generator[str, None, None]:
    medication = Medication(
        uuid=generate_uuid(), name="InsulinPlus", sct_code="2345", unit="units", tags=[]
    )
    db.session.add(medication)
    db.session.commit()

    yield medication.uuid

    try:
        db.session.delete(medication)
    except InvalidRequestError:
        pass
    db.session.commit()


@pytest.fixture
def med_with_tags_uuid() -> Generator[str, None, None]:
    medication = Medication(
        uuid=generate_uuid(),
        name="Adrenaline",
        sct_code="12345678",
        unit="mmol",
        tags=["gdm", "tag1", "tag2"],
    )

    db.session.add(medication)
    db.session.commit()

    yield medication.uuid

    try:
        db.session.delete(medication)
    except InvalidRequestError:
        pass
    db.session.commit()
