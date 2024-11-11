from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("cars/", include("cars.urls")),
    path("locations/", include("locations.urls")),
    path("", include("trips.urls")),
    path("users/", include("users.urls")),
    path("admin/", admin.site.urls),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("refresh/", TokenRefreshView.as_view(), name="refresh"),
]
