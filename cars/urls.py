from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_cars, name="get_cars"),
    path("<int:id>/", views.car_detail, name="car_detail"),
]
