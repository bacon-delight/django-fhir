from rest_framework import serializers

# Models
from .models import PatientModel

# Serializers
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientModel
        fields = "__all__"
