from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("baseR4/", include("baseR4.urls")),
    # path('admin/', admin.site.urls),
]
