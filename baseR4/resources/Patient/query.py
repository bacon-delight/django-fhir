from django.db import models
from rest_framework import serializers

# Utilities
from common.utilities import (
    list_to_iterable_tuple_list,
)

# Data Types
from ...valuesets.AdministrativeGender import AdministrativeGender
from ...datatypes.primitives import (
    FHIR_DATATYPE_BOOLEAN,
    FHIR_DATATYPE_STRING,
)

# Available Query Parameters
query_params = ["active", "gender", "address-state", "address-city"]


# Model
class PatientQueryModel(models.Model):
    active = FHIR_DATATYPE_BOOLEAN()
    gender = models.CharField(
        max_length=7,
        choices=list_to_iterable_tuple_list(AdministrativeGender),
        blank=True,
    )
    address_city = FHIR_DATATYPE_STRING()
    address_state = FHIR_DATATYPE_STRING()


# Serializer
class PatientQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientQueryModel
        fields = query_params
        extra_kwargs = {
            "address-city": {"source": "address_city"},
            "address-state": {"source": "address_state"},
        }
