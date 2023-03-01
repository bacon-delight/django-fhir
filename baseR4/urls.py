from django.urls import path

# from rest_framework.urlpatterns import format_suffix_patterns

# Resources
from .resources.Patient.views import PatientViews
from .resources.Encounter.views import EncounterViews
# Patterns
# urlpatterns = [
#     path("Patient", PatientViews.as_view()),
#     path("Patient/<id>", PatientViews.as_view()),
# ]

urlpatterns = [
    path("Patient", PatientViews.as_view({"get": "list", "post": "create"})),
    path("Patient/<id>", PatientViews.as_view({"get": "retrieve"})),
    path("Encounter", EncounterViews.as_view({"get": "list", "post": "create"})),
    path("Encounter/<id>", EncounterViews.as_view({"get": "retrieve"})),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
