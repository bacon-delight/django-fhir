from django.db import models

# Utilities
from common.utilities import (
    list_to_iterable_tuple_list,
    string_to_tuple,
    UUID_MAX_LENGTH,
)

# Data Types
from ...valuesets.AdministrativeGender import AdministrativeGender
from ...datatypes.primitives import (
    FHIR_DATATYPE_BOOLEAN,
    FHIR_DATATYPE_DATE,
    FHIR_DATATYPE_DATETIME,
    FHIR_DATATYPE_INTEGER,
)
from ..types import RESOURCE_TYPE_Patient

# Models
class PatientModel(models.Model):
    _id = models.CharField(max_length=UUID_MAX_LENGTH, blank=False)
    resourceType = models.CharField(
        max_length=7, choices=[string_to_tuple(RESOURCE_TYPE_Patient)], blank=False
    )
    # identifier - Handled by Serializer
    active = FHIR_DATATYPE_BOOLEAN()
    # name
    # telecom
    gender = models.CharField(
        max_length=7,
        choices=list_to_iterable_tuple_list(AdministrativeGender),
        blank=True,
    )
    birthDate = FHIR_DATATYPE_DATE()
    deceasedBoolean = FHIR_DATATYPE_BOOLEAN()
    deceasedDateTime = FHIR_DATATYPE_DATETIME()
    # address
    # maritalStatus
    multipleBirthBoolean = FHIR_DATATYPE_BOOLEAN()
    multipleBirthInteger = FHIR_DATATYPE_INTEGER()
    # photo
    # contact
    # communication
    # generalPractitioner
    # managingOrganization
    # link
