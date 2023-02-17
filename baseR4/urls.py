from django.urls import path
from baseR4 import views

# from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("Patient", views.Patient.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
