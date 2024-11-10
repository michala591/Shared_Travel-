from rest_framework import serializers

from cars.models import Car
from users.models import User
from locations.models import Locations
from .models import Trips


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"  # Add more fields as needed


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"  # Add more fields as needed


class TripsLocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locations
        fields = ["city", "zone"]


class tripsSerializer(serializers.ModelSerializer):
    car = CarSerializer()  # Use the nested Car serializer
    origin_station = TripsLocationsSerializer()
    destination_station = TripsLocationsSerializer()

    class Meta:
        model = Trips
        fields = "__all__"


class TripsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trips
        fields = ["id"]


class UserSerializer(serializers.ModelSerializer):
    trips = TripsSerializer(
        many=True, read_only=True
    )  # List of trips the user is associated with

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "trips",
            "user_type",
            "is_active",
        ]  # Customize as needed


class TripsLocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locations
        fields = ["city", "zone"]


class SearchTripsSerializer(serializers.ModelSerializer):
    origin_station = TripsLocationsSerializer()
    destination_station = TripsLocationsSerializer()

    class Meta:
        model = Trips
        fields = [
            "car",
            "days",
            "departure_time",
            "return_time",
            "origin_station",
            "destination_station",
        ]
