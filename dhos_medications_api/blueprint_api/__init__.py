from typing import Dict, List, Optional

import connexion
import flask
from flask import Response

from dhos_medications_api.blueprint_api import controller

api_blueprint = flask.Blueprint("medications", __name__)


@api_blueprint.route("/medication/<medication_id>", methods=["GET"])
def get_medication(medication_id: str) -> Response:
    """---
    get:
      summary: Get medication
      description: Get a medication by UUID
      tags: [medication]
      parameters:
        - name: medication_id
          in: path
          required: true
          description: The medication UUID
          schema:
            type: string
            example: '18439f36-ffa9-42ae-90de-0beda299cd37'
      responses:
        '200':
          description: The requested medication
          content:
            application/json:
              schema: MedicationResponse
        default:
          description: Error, e.g. 404 Not Found, 503 Service Unavailable
          content:
            application/json:
              schema: Error
    """
    medication: Dict = controller.get_medication(medication_uuid=medication_id)
    return flask.jsonify(medication)


@api_blueprint.route("/medication", methods=["GET"])
def get_all_medications(tag: Optional[str] = None) -> Response:
    """---
    get:
      summary: Get all medications
      description: Get a list of all medications
      tags: [medication]
      parameters:
        - name: tag
          in: query
          required: false
          description: Tag to filter medications by
          schema:
            type: string
            example: diabetes
      responses:
        '200':
          description: A list of all medications
          content:
            application/json:
              schema:
                type: array
                items: MedicationResponse
        default:
          description: >-
              Error, e.g. 400 Bad Request, 404 Not Found, 503 Service Unavailable
          content:
            application/json:
              schema: Error
    """
    medications: List[Dict] = controller.get_all_medications(tag=tag)
    return flask.jsonify(medications)


@api_blueprint.route("/medication", methods=["POST"])
def create_medication() -> Response:
    """---
    post:
      summary: Create new medication
      description: Create a new medication
      tags: [medication]
      requestBody:
        description: JSON body containing the medication
        required: true
        content:
          application/json:
            schema: MedicationRequest
      responses:
        '200':
          description: The new medication
          content:
            application/json:
              schema: MedicationResponse
        default:
          description: >-
              Error, e.g. 400 Bad Request, 404 Not Found, 503 Service Unavailable
          content:
            application/json:
              schema: Error
    """
    medication_details: Dict = connexion.request.get_json()
    new_medication: Dict = controller.create_medication(
        medication_details=medication_details
    )
    return flask.jsonify(new_medication)


@api_blueprint.route("/medication/<medication_id>", methods=["DELETE"])
def delete_medication(medication_id: str) -> Response:
    """---
    delete:
      summary: Delete medication
      description: Delete a medication by UUID
      tags: [medication]
      parameters:
        - name: medication_id
          in: path
          required: true
          description: The medication UUID
          schema:
            type: string
            example: '18439f36-ffa9-42ae-90de-0beda299cd37'
      responses:
        '200':
          description: The deleted medication
          content:
            application/json:
              schema: MedicationResponse
        default:
          description: >-
              Error, e.g. 400 Bad Request, 404 Not Found, 503 Service Unavailable
          content:
            application/json:
              schema: Error
    """
    deleted_medication: Dict = controller.delete_medication(
        medication_uuid=medication_id
    )
    return flask.jsonify(deleted_medication)


@api_blueprint.route("/medication/<medication_id>", methods=["PATCH"])
def patch_medication(medication_id: str) -> Response:
    """---
    patch:
      summary: Update medication
      description: Update a medication by UUID
      tags: [medication]
      parameters:
        - name: medication_id
          in: path
          required: true
          description: The medication UUID
          schema:
            type: string
            example: '18439f36-ffa9-42ae-90de-0beda299cd37'
      requestBody:
        description: JSON body containing the medication fields to be updated
        required: true
        content:
          application/json:
            schema: MedicationPatchRequest
      responses:
        '200':
          description: The updated medication
          content:
            application/json:
              schema: MedicationResponse
        default:
          description: >-
              Error, e.g. 400 Bad Request, 404 Not Found, 503 Service Unavailable
          content:
            application/json:
              schema: Error
    """
    medication_details: Dict = connexion.request.get_json()
    updated_medication: Dict = controller.update_medication(
        medication_uuid=medication_id, medication_details=medication_details
    )
    return flask.jsonify(updated_medication)
