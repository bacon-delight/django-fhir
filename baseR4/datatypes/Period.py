from django.db import models
from rest_framework import serializers

# Utilities
from .primitives import FHIR_DATATYPE_DATETIME

# https://hl7.org/fhir/datatypes.html#Period
class PeriodModel(models.Model):
    start = FHIR_DATATYPE_DATETIME()
    end = FHIR_DATATYPE_DATETIME()


class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeriodModel
        fields = "__all__"
