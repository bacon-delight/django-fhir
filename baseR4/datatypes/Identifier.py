from django.db import models
from rest_framework import serializers

# Utilities
from common.utilities import list_to_iterable_tuple_list
from common.error_messages import generate_error_message_invalid_choice

# Data Types
from .primitives import FHIR_DATATYPE_URI, FHIR_DATATYPE_STRING
from ..valuesets.IdentifierUse import (
    IdentifierUse,
    IdentifierUse_ContentLogicalDefinition,
)

# Models & Serializers
from .CodeableConcept import CodeableConceptSerializer
from .Period import PeriodSerializer

# https://hl7.org/fhir/datatypes.html#Coding
class IdentifierModel(models.Model):
    use = models.CharField(
        max_length=9,
        choices=list_to_iterable_tuple_list(IdentifierUse),
        blank=True,
    )
    # type - Handled by Serializer
    system = FHIR_DATATYPE_URI()
    value = FHIR_DATATYPE_STRING()
    # period - Handled by Serializer
    # assigner


class IdentifierSerializer(serializers.ModelSerializer):
    type = CodeableConceptSerializer(many=False, required=False)
    period = PeriodSerializer(many=False, required=False)

    class Meta:
        model = IdentifierModel
        fields = "__all__"
        extra_kwargs = {
            "use": {
                "error_messages": {
                    generate_error_message_invalid_choice(
                        data_definition=IdentifierUse_ContentLogicalDefinition,
                    )
                }
            }
        }
