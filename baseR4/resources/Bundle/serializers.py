from rest_framework import serializers

# Utilities
from common.error_messages import generate_error_message_invalid_choice

# Models & Serializers
from .models import BundleModel, bundle_entry_model, bundle_link_model
from ..Patient.serializers import PatientSerializer

# Data Types
from ...valuesets.BundleType import BundleType_ContentLogicalDefinition


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
        extra_kwargs = {
            "type": {
                "error_messages": {
                    generate_error_message_invalid_choice(
                        data_definition=BundleType_ContentLogicalDefinition,
                    )
                }
            }
        }
