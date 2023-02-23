from django.db import models
from rest_framework import serializers

# Utilities
from utilities import list_to_iterable_tuple_list
from common.error_messages import error_message_invalid_choice

# Data Types
from .primitives import FHIR_DATATYPE_STRING, FHIR_DATATYPE_CODE
from ..valuesets.AddressUse import AddressUse, AddressUse_ContentLogicalDefinition

# https://hl7.org/fhir/datatypes.html#Address
class AddressModel(models.Model):
    use = models.CharField(
        max_length=7, choices=list_to_iterable_tuple_list(AddressUse), blank=True
    )


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressModel
        fields = "__all__"
        extra_kwargs = {
            "use": {
                "error_messages": {
                    error_message_invalid_choice(
                        data_definition=AddressUse_ContentLogicalDefinition,
                    )
                }
            }
        }
