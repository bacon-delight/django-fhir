from django.db import models

# Utilities
from utilities import list_to_iterable_tuple_list, UUID_MAX_LENGTH
from ...valuesets.AdministrativeGender import AdministrativeGender

# Resource Types
RESOURCE_TYPE_Patient = "Patient"

# Models
class PatientModel(models.Model):
    _id = models.CharField(max_length=UUID_MAX_LENGTH, blank=False)
    # identifier
    active = models.BooleanField(blank=True)
    # name
    # telecom
    gender = models.CharField(
        max_length=7,
        choices=list_to_iterable_tuple_list(AdministrativeGender),
        blank=True,
    )
    birthDate = models.DateField(blank=True)
    deceasedBoolean = models.BooleanField(default=True)
    deceasedDateTime = models.DateTimeField(blank=True)
    # address
    # maritalStatus
    multipleBirthBoolean = models.BooleanField(blank=True)
    multipleBirthInteger = models.IntegerField(blank=True)
    # photo
    # contact
    # communication
    # generalPractitioner
    # managingOrganization
    # link
