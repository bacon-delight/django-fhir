from django.db import models
from rest_framework import serializers
from django.core.validators import RegexValidator

# Utilities
from common.error_messages import generate_error_message

# https://hl7.org/fhir/datatypes.html#boolean
def FHIR_DATATYPE_BOOLEAN(blank=True):
    return models.BooleanField(blank=blank)


# https://hl7.org/fhir/datatypes.html#integer
def FHIR_DATATYPE_INTEGER(blank=True):
    return models.IntegerField(
        blank=blank,
        validators=[
            RegexValidator(
                regex="^[0]|[-+]?[1-9][0-9]*$",
                message=generate_error_message(
                    data_definition="https://hl7.org/fhir/datatypes.html#integer"
                ),
            ),
        ],
    )


# https://hl7.org/fhir/datatypes.html#string
def FHIR_DATATYPE_STRING(blank=True):
    return models.CharField(
        max_length=1024 * 1024,
        blank=blank,
        validators=[
            RegexValidator(
                regex="^[ \r\n\t\S]+$",
                message=generate_error_message(
                    data_definition="https://hl7.org/fhir/datatypes.html#string"
                ),
            ),
        ],
    )


def FHIR_DATATYPE_STRING_LIST(blank=True):
    return serializers.ListSerializer(
        child=serializers.CharField(max_length=1024 * 1024),
        required=blank,
    )


# https://hl7.org/fhir/datatypes.html#uri
def FHIR_DATATYPE_URI(blank=True):
    # return models.URLField(blank=blank)
    return models.CharField(
        max_length=1024 * 1024,
        blank=blank,
        validators=[
            RegexValidator(
                regex="^\S*$",
                message=generate_error_message(
                    data_definition="https://hl7.org/fhir/datatypes.html#uri"
                ),
            ),
        ],
    )


# https://hl7.org/fhir/datatypes.html#instant
def FHIR_DATATYPE_INSTANT(blank=True):
    return models.DateTimeField(
        blank=blank,
        # validators=[
        #     RegexValidator(
        #         regex="^([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])T([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\.[0-9]+)?(Z|(\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00))$",
        #         message="Instant doesn't adhere to https://hl7.org/fhir/datatypes.html#instant",
        #     ),
        # ],
    )


# https://hl7.org/fhir/datatypes.html#date
def FHIR_DATATYPE_DATE(blank=True):
    return models.DateField(
        blank=blank,
        validators=[
            RegexValidator(
                regex="^([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)(-(0[1-9]|1[0-2])(-(0[1-9]|[1-2][0-9]|3[0-1]))?)?$",
                message=generate_error_message(
                    data_definition="https://hl7.org/fhir/datatypes.html#date"
                ),
            ),
        ],
    )


# https://hl7.org/fhir/datatypes.html#dateTime
def FHIR_DATATYPE_DATETIME(blank=True):
    return models.DateTimeField(
        blank=blank,
        validators=[
            RegexValidator(
                regex="^([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)(-(0[1-9]|1[0-2])(-(0[1-9]|[1-2][0-9]|3[0-1])(T([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\.[0-9]+)?(Z|(\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00)))?)?)?$",
                message=generate_error_message(
                    data_definition="https://hl7.org/fhir/datatypes.html#dateTime"
                ),
            ),
        ],
    )


# https://hl7.org/fhir/datatypes.html#code
def FHIR_DATATYPE_CODE(blank=True):
    return models.CharField(
        max_length=1024 * 1024,
        blank=blank,
        validators=[
            RegexValidator(
                regex="^[^\s]+(\s[^\s]+)*$",
                message=generate_error_message(
                    data_definition="https://hl7.org/fhir/datatypes.html#code"
                ),
            ),
        ],
    )


# https://hl7.org/fhir/datatypes.html#unsignedInt
def FHIR_DATATYPE_UNSIGNEDINT(blank=True):
    return models.IntegerField(
        blank=blank,
        validators=[
            RegexValidator(
                regex="^[0]|([1-9][0-9]*)$",
                message=generate_error_message(
                    data_definition="https://hl7.org/fhir/datatypes.html#unsignedInt"
                ),
            ),
        ],
    )
