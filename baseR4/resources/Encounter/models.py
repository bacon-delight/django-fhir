from django.db import models

# Utilities
from common.utilities import (
    list_to_iterable_tuple_list,
    string_to_tuple,
    UUID_MAX_LENGTH,
)

# Data Types
from ...datatypes.primitives import (
    FHIR_DATATYPE_BOOLEAN,
    FHIR_DATATYPE_DATE,
    FHIR_DATATYPE_DATETIME,
    FHIR_DATATYPE_INTEGER,
    FHIR_DATATYPE_CODE
)
from ..types import RESOURCE_TYPE_Encounter

# Models
class EncounterModel(models.Model):
    _id = models.CharField(max_length=UUID_MAX_LENGTH, blank=False)
    resourceType = models.CharField(
        max_length=7, choices=[string_to_tuple(RESOURCE_TYPE_Encounter)], blank=False
    )
    # identifier - Handled by Serializer
    # name
    # telecom
    status = models.CharField(
        max_length=7,
        choices=list_to_iterable_tuple_list(EncounterStatus),
        blank=True,
    )

    
  