from rest_framework import serializers
from .models import Trips


class tripsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trips
        fields = "__all__"  # You can also specify fields explicitly if needed
