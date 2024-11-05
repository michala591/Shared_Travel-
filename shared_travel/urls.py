from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("cars/", include("cars.urls")),
    path("locations/", include("locations.urls")),
    path("trips/", include("trips.urls")),
    path("users/", include("users.urls")),
    path("admin/", admin.site.urls),
]
