from django.db import models
from django.core.validators import RegexValidator

# https://hl7.org/fhir/datatypes.html#boolean
def FHIR_DATATYPE_BOOLEAN(blank=True):
    return models.BooleanField(blank=blank)


# https://hl7.org/fhir/datatypes.html#string
def FHIR_DATATYPE_STRING(blank=True):
    return models.CharField(
        max_length=1024 * 1024,
        blank=blank,
        validators=[
            RegexValidator(
                regex="^[ \r\n\t\S]+$",
                message="String doesn't adhere to https://hl7.org/fhir/datatypes.html#string",
            ),
        ],
    )


# https://hl7.org/fhir/datatypes.html#uri
def FHIR_DATATYPE_URI(blank=True):
    return models.URLField(blank=blank)


# https://hl7.org/fhir/datatypes.html#code
def FHIR_DATATYPE_CODE(blank=True):
    return models.CharField(
        max_length=1024 * 1024,
        blank=blank,
        validators=[
            RegexValidator(
                regex="^[^\s]+(\s[^\s]+)*$",
                message="Code doesn't adhere to https://hl7.org/fhir/datatypes.html#code",
            ),
        ],
    )
