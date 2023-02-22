from rest_framework import serializers

# Models & Serializers
from .models import BundleModel, bundle_entry_model, bundle_link_model

# from ...datatypes.Identifier import IdentifierSerializer
from ..Patient.serializers import PatientSerializer

# Serializers
class bundle_entry_serializer(serializers.ModelSerializer):
    resource = PatientSerializer(many=False, required=False)

    class Meta:
        model = bundle_entry_model
        fields = "__all__"


class bundle_link_serializer(serializers.ModelSerializer):
    class Meta:
        model = bundle_link_model
        fields = "__all__"


class BundleSerializer(serializers.ModelSerializer):
    entry = bundle_entry_serializer(many=True, required=False)
    link = bundle_link_serializer(many=True, required=False)

    class Meta:
        model = BundleModel
        fields = "__all__"
