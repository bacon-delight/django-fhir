from django.urls import path

# from rest_framework.urlpatterns import format_suffix_patterns

# Resources
from .resources.Patient.views import PatientViews

# Patterns
urlpatterns = [
    path("Patient", PatientViews.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
