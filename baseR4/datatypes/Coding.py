from django.db import models
from rest_framework import serializers

# Utilities
from .primitives import (
    FHIR_DATATYPE_BOOLEAN,
    FHIR_DATATYPE_STRING,
    FHIR_DATATYPE_CODE,
    FHIR_DATATYPE_URI,
)

# https://hl7.org/fhir/datatypes.html#Coding
class CodingModel(models.Model):
    system = FHIR_DATATYPE_URI()
    version = FHIR_DATATYPE_STRING()
    code = FHIR_DATATYPE_CODE()
    display = FHIR_DATATYPE_STRING()
    userSelected = FHIR_DATATYPE_BOOLEAN()


class CodingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodingModel
        fields = "__all__"
