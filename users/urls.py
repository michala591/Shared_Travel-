from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_users, name="user"),
    path("<int:id>/", views.user_detail, name="user_detail"),
]
