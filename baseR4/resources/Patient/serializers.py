from rest_framework import serializers

# Models & Serializers
from .models import PatientModel
from ...datatypes.CodeableConcept import CodeableConceptSerializer

# Serializers
class PatientSerializer(serializers.ModelSerializer):
    maritalStatus = CodeableConceptSerializer(required=False)

    class Meta:
        model = PatientModel
        fields = "__all__"
