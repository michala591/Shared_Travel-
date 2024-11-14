from django.urls import path
from . import views

urlpatterns = [
    path("car_id", views.car_id, name="car_id"),
    path("my_car/", views.car_detail, name="car_detail"),
]
