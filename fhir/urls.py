from django.contrib import admin
from django.urls import include, path
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path("baseR4/", include("baseR4.urls")),
    path(
        "metadata",
        get_schema_view(
            title="Django FHIR Server",
            description="Capability Statement",
            version="0.0.1",
        ),
    ),
]
