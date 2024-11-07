from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_trips, name="trip"),
    path("<int:id>/", views.trip_detail, name="trip_detail"),
]
