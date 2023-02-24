from django.urls import include, path
from rest_framework.schemas import get_schema_view
from django.views.decorators.cache import cache_control
from django.contrib.staticfiles.views import serve
from django.conf.urls.static import static

# Utilities
from . import settings
from common.swagger import swagger_url_patterns


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

urlpatterns += static(
    settings.STATIC_URL, view=cache_control(no_cache=True, must_revalidate=True)(serve)
)
urlpatterns += swagger_url_patterns
