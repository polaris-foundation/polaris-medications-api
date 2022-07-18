from typing import Dict, List, Optional

from flask_batteries_included.config import is_production_environment
from flask_batteries_included.helpers.error_handler import DuplicateResourceException
from flask_batteries_included.sqldb import db, generate_uuid
from she_logging import logger

from dhos_medications_api.models.medication import Medication


def create_medication(medication_details: Dict) -> Dict:
    logger.debug("Creating medication", extra={"medication_data": medication_details})
    if _medication_name_exists(name=medication_details["name"]):
        raise DuplicateResourceException(
            f"Medication '{medication_details['name']}' already exists"
        )
    medication = Medication()
    medication.name = medication_details["name"]
    medication.unit = medication_details["unit"]
    medication.sct_code = medication_details["sct_code"]
    medication.tags = medication_details.get("tags", [])
    if medication_details.get("uuid", None) and not is_production_environment():
        medication.uuid = medication_details["uuid"]
    else:
        medication.uuid = generate_uuid()
    db.session.add(medication)
    db.session.commit()
    return medication.to_dict()


def get_all_medications(tag: Optional[str] = None) -> List[Dict]:
    logger.debug("Getting all medications")
    medications: List[Medication] = Medication.query.order_by(
        Medication.name, Medication.created
    ).all()
    if tag:
        logger.debug("Filtering medications by tag %s", tag)
        return [m.to_dict() for m in medications if tag in m.tags]
    else:
        return [m.to_dict() for m in medications]


def get_medication(medication_uuid: str) -> Dict:
    medication: Medication = Medication.query.filter_by(
        uuid=medication_uuid
    ).first_or_404()
    return medication.to_dict()


def delete_medication(medication_uuid: str) -> Dict:
    medication: Medication = Medication.query.filter_by(
        uuid=medication_uuid
    ).first_or_404()
    medication.delete()
    db.session.commit()
    return medication.to_dict()


def update_medication(medication_uuid: str, medication_details: Dict) -> Dict:
    medication = Medication.query.filter_by(uuid=medication_uuid).first_or_404()
    logger.debug(
        "Patching medication with UUID %s",
        medication_uuid,
        extra={"medication_data": medication_details},
    )
    if len(medication_details) == 0:
        raise ValueError("No details to update")

    if "name" in medication_details:
        if medication_details["name"] != medication.name and _medication_name_exists(
            name=medication_details["name"]
        ):
            raise DuplicateResourceException(
                "Cannot change 'name' to match existing medication"
            )
        medication.name = medication_details["name"]

    if "unit" in medication_details:
        medication.unit = medication_details["unit"]

    if "sct_code" in medication_details:
        medication.sct_code = medication_details["sct_code"]

    if "tags" in medication_details:
        medication.tags = medication_details["tags"]

    db.session.commit()
    return medication.to_dict()


def _medication_name_exists(name: str) -> bool:
    is_existing = Medication.query.filter(Medication.name.ilike(name)).first()
    return is_existing is not None
