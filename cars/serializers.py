from rest_framework import serializers

from users.models import User
from .models import Car


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "id", "name"  # Add more fields as needed


class CarSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True)

    class Meta:
        model = Car
        fields = "__all__"
