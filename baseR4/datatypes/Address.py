from django.db import models
from rest_framework import serializers

# Utilities
from common.utilities import list_to_iterable_tuple_list
from common.error_messages import generate_error_message_invalid_choice

# Data Types
from .primitives import FHIR_DATATYPE_STRING, FHIR_DATATYPE_STRING_LIST
from ..valuesets.AddressUse import AddressUse, AddressUse_ContentLogicalDefinition
from ..valuesets.AddressType import AddressType, AddressType_ContentLogicalDefinition
from .Period import PeriodSerializer

# https://hl7.org/fhir/datatypes.html#Address
class AddressModel(models.Model):
    use = models.CharField(
        max_length=7, choices=list_to_iterable_tuple_list(AddressUse), blank=True
    )
    type = models.CharField(
        max_length=8, choices=list_to_iterable_tuple_list(AddressType), blank=True
    )
    text = FHIR_DATATYPE_STRING()
    # line - Handled by Serializer
    city = FHIR_DATATYPE_STRING()
    district = FHIR_DATATYPE_STRING()
    state = FHIR_DATATYPE_STRING()
    postalCode = FHIR_DATATYPE_STRING()
    country = FHIR_DATATYPE_STRING()
    # period - Handled by Serializer


class AddressSerializer(serializers.ModelSerializer):
    line = FHIR_DATATYPE_STRING_LIST()
    period = PeriodSerializer(many=False, required=False)

    class Meta:
        model = AddressModel
        fields = "__all__"
        extra_kwargs = {
            "use": {
                "error_messages": {
                    generate_error_message_invalid_choice(
                        data_definition=AddressUse_ContentLogicalDefinition,
                    )
                }
            },
            "type": {
                "error_messages": {
                    generate_error_message_invalid_choice(
                        data_definition=AddressType_ContentLogicalDefinition,
                    )
                }
            },
        }
