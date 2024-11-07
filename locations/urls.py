from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_locations, name="location"),
    path("<int:id>/", views.location_detail, name="location_detail"),
]
