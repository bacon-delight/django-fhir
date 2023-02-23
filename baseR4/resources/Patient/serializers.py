from rest_framework import serializers

# Utilities
from common.error_messages import generate_error_message_invalid_choice

# Models & Serializers
from .models import PatientModel

# Data Types
from ...datatypes.CodeableConcept import CodeableConceptSerializer
from ...datatypes.Identifier import IdentifierSerializer
from ...datatypes.Address import AddressSerializer
from ...valuesets.AdministrativeGender import (
    AdministrativeGender_ContentLogicalDefinition,
)

# Serializers
class PatientSerializer(serializers.ModelSerializer):
    identifier = IdentifierSerializer(many=True, required=False)
    maritalStatus = CodeableConceptSerializer(many=False, required=False)
    address = AddressSerializer(many=True, required=False)

    class Meta:
        model = PatientModel
        fields = "__all__"
        extra_kwargs = {
            "gender": {
                "error_messages": {
                    generate_error_message_invalid_choice(
                        data_definition=AdministrativeGender_ContentLogicalDefinition,
                    )
                }
            }
        }
