from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_trips, name="trip"),
    path("active_trips/", views.get_active_trips, name="get_active_trips"),
    path("<int:id>/", views.trip_detail, name="trip_detail"),
    path("<int:id>/users/", views.get_passengers, name="get_passengers"),
    path("<int:id>/invite/", views.invite_to_trip, name="invite_to_trip"),
    path("search/", views.search_trips, name="search_trips"),
]
