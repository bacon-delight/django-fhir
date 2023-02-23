from rest_framework import serializers

# Models & Serializers
from .models import PatientModel
from ...datatypes.CodeableConcept import CodeableConceptSerializer
from ...datatypes.Identifier import IdentifierSerializer
from ...datatypes.Address import AddressSerializer

# Serializers
class PatientSerializer(serializers.ModelSerializer):
    identifier = IdentifierSerializer(many=True, required=False)
    maritalStatus = CodeableConceptSerializer(many=False, required=False)
    address = AddressSerializer(many=True, required=False)

    class Meta:
        model = PatientModel
        fields = "__all__"
