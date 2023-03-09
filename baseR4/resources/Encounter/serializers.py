from rest_framework import serializers

# Utilities
from common.error_messages import generate_error_message_invalid_choice

# Models & Serializers
from .models import EncounterModel

# Data Types
from ...datatypes.CodeableConcept import CodeableConceptSerializer
from ...datatypes.Identifier import IdentifierSerializer
from ...datatypes.Address import AddressSerializer
from ...valuesets.AdministrativeGender import (
    AdministrativeGender_ContentLogicalDefinition,
)
from .Period import PeriodSerializer

# Serializers
class EncounterSerializer(serializers.ModelSerializer):
    identifier = IdentifierSerializer(many=True, required=False)
   # class = CodingSerializer(many=True, required=True)
    type = CodeableConceptSerializer(many=False, required=False)
    serviceType = CodeableConceptSerializer(many=False, required=False)
    priority = CodeableConceptSerializer(many=False, required=False)
    reasonCode = CodeableConceptSerializer(many=False, required=False)
    address = AddressSerializer(many=True, required=False)
    period = PeriodSerializer(many=False, required=False)
    statusHistory = statusHistorySerializer(many=True, required=false)
    length = DurationSerializer(many=False, required=false)
    
    class Meta:
        model = EncounterModel
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