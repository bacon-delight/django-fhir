from django.db import models

# Utilities
from utilities import list_to_iterable_tuple_list
from baseR4.valuesets.AdministrativeGender import AdministrativeGender

# Resource Types
RESOURCE_TYPE_Patient = "Patient"

# Models
class PatientModel(models.Model):
    _id = models.CharField(max_length=60, blank=False)
    # identifier
    active = models.BooleanField(blank=True)
    # name
    # telecom
    gender = models.CharField(
        max_length=7,
        blank=True,
        choices=list_to_iterable_tuple_list(AdministrativeGender),
    )
    birthDate = models.DateField(blank=True)
