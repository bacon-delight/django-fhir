from django.db import models
from rest_framework import serializers

# Models & Serializers
from .Coding import CodingSerializer

# Data Types
from .primitives import FHIR_DATATYPE_STRING

# https://hl7.org/fhir/datatypes.html#CodeableConcept
class CodeableConceptModel(models.Model):
    # coding - Handled by Serializer
    text = FHIR_DATATYPE_STRING()


class CodeableConceptSerializer(serializers.ModelSerializer):
    coding = CodingSerializer(many=True, required=False)

    class Meta:
        model = CodeableConceptModel
        fields = "__all__"
