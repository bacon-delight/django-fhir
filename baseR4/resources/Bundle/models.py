from django.db import models

# Utilities
from utilities import UUID_MAX_LENGTH, string_to_tuple, list_to_iterable_tuple_list

# Data Types
from ..types import RESOURCE_TYPE_Bundle
from ...valuesets.BundleType import BundleType
from ...datatypes.primitives import (
    FHIR_DATATYPE_INSTANT,
    FHIR_DATATYPE_UNSIGNEDINT,
    FHIR_DATATYPE_URI,
)
from ...valuesets.IANA_LinkRelations import IANA_LinkRelations

# Models
class bundle_entry_model(models.Model):
    # link
    fullUrl = FHIR_DATATYPE_URI()
    # resource - Handled by Serializer
    # search
    # request
    # response


class bundle_link_model(models.Model):
    relation = models.CharField(
        max_length=25,
        choices=list_to_iterable_tuple_list(IANA_LinkRelations),
        blank=True,
    )
    url = FHIR_DATATYPE_URI()


class BundleModel(models.Model):
    _id = models.CharField(max_length=UUID_MAX_LENGTH, blank=False)
    resourceType = models.CharField(
        max_length=7, choices=[string_to_tuple(RESOURCE_TYPE_Bundle)], blank=False
    )
    # identifier - Handled by Serializer
    type = models.CharField(
        max_length=20, choices=list_to_iterable_tuple_list(BundleType), blank=False
    )
    timestamp = FHIR_DATATYPE_INSTANT()
    total = FHIR_DATATYPE_UNSIGNEDINT()
    # link
    # entry
