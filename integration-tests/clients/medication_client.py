from typing import Dict, Optional

import requests
from environs import Env
from requests import Response

base_url = Env().str("DHOS_MEDICATIONS_BASE_URL", "http://dhos-medications-api:5000")


def create_medication(body: Dict) -> Response:
    return requests.post(
        f"{base_url}/dhos/v1/medication",
        timeout=15,
        json=body,
    )


def get_medication(uuid: str) -> Response:
    return requests.get(
        f"{base_url}/dhos/v1/medication/{uuid}",
        timeout=15,
    )


def get_all_medications(tag: Optional[str] = None) -> Response:
    params: Dict[str, str] = {"tag": tag} if tag else {}
    return requests.get(
        f"{base_url}/dhos/v1/medication",
        timeout=15,
        params=params,
    )


def update_medication(uuid: str, body: Dict) -> Response:
    return requests.patch(
        f"{base_url}/dhos/v1/medication/{uuid}",
        timeout=15,
        json=body,
    )


def delete_medication(uuid: str) -> Response:
    return requests.delete(
        f"{base_url}/dhos/v1/medication/{uuid}",
        timeout=15,
    )
