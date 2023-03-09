from django.db import models
from rest_framework import serializers

# Utilities
from common.utilities import list_to_iterable_tuple_list
from common.error_messages import generate_error_message_invalid_choice

#valuesets
from ...valuesets.EncounterStatus import EncounterStatus

# Data Types
from .Period import PeriodSerializer

class statusHistoryModel(models.Model):
    status = models.CharField(
        max_length=7,
        choices=list_to_iterable_tuple_list(EncounterStatus),
        blank=True,)

    period = PeriodSerializer(many=False, required=False)

class statusHistorySerializer(serializers.ModelSerializer):
     class Meta:
        model = statusHistoryModel
        fields = "__all__"
    
