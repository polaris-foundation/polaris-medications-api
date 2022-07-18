from datetime import datetime
from typing import TypedDict

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from flask_batteries_included.helpers.apispec import (
    FlaskBatteriesPlugin,
    Identifier,
    initialise_apispec,
    openapi_schema,
)
from marshmallow import EXCLUDE, Schema, fields, validate

dhos_medications_api_spec: APISpec = APISpec(
    version="1.1.0",
    openapi_version="3.0.3",
    title="DHOS Medications API",
    info={
        "description": "The DHOS Medications API is responsible for storing and retrieving information about medications."
    },
    plugins=[FlaskPlugin(), MarshmallowPlugin(), FlaskBatteriesPlugin()],
)

initialise_apispec(dhos_medications_api_spec)


@openapi_schema(dhos_medications_api_spec)
class MedicationSchema(Schema):
    class Meta:
        title = "Medication fields common to request and response"
        unknown = EXCLUDE
        ordered = True

        class Dict(TypedDict, total=False):
            sct_code: str
            name: str
            unit: str
            deleted: datetime

    sct_code = fields.String(
        required=True,
        example="109081006",
        description="The SCT code of the medication",
        validate=validate.Length(min=1),
    )
    name = fields.String(
        required=True,
        example="Metformin",
        description="The name of the medication",
        validate=validate.Length(min=1),
    )
    unit = fields.String(
        required=True,
        example="mmol",
        description="The unit of the medication",
        validate=validate.Length(min=1),
    )
    tags = fields.List(
        fields.String(description="Tag name", required=False, example="diabetes"),
        description="Tags with which the medication is associated",
        required=False,
    )


@openapi_schema(dhos_medications_api_spec)
class MedicationRequest(MedicationSchema):
    class Meta:
        title = "Medication request"
        unknown = EXCLUDE
        ordered = True

        class Dict(TypedDict, MedicationSchema.Meta.Dict, total=False):
            pass


@openapi_schema(dhos_medications_api_spec)
class MedicationPatchRequest(Schema):
    class Meta:
        title = "Medication PATCH request"
        unknown = EXCLUDE
        ordered = True

        class Dict(TypedDict, MedicationSchema.Meta.Dict, total=False):
            pass

    sct_code = fields.String(
        required=False,
        example="109081006",
        description="The SCT code of the medication",
        validate=validate.Length(min=1),
    )
    name = fields.String(
        required=False,
        example="Metformin",
        description="The name of the medication",
        validate=validate.Length(min=1),
    )
    unit = fields.String(
        required=False,
        example="mmol",
        description="The unit of the medication",
        validate=validate.Length(min=1),
    )
    tags = fields.List(
        fields.String(description="Tag name", required=False, example="diabetes"),
        description="Tags with which the medication is associated",
        required=False,
    )


@openapi_schema(dhos_medications_api_spec)
class MedicationResponse(Identifier, MedicationSchema):
    class Meta:
        title = "Medication response"
        unknown = EXCLUDE
        ordered = True

        class Dict(TypedDict, MedicationSchema.Meta.Dict, total=False):
            pass
