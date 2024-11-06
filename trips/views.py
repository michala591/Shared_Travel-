from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import tripsSerializer
from .models import Trips


@api_view(["GET", "POST"])
def get_trips(request):
    if request.method == "GET":
        trips = Trips.objects.all()
        serializer = tripsSerializer(trips, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = tripsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def trip_detail(request, id):
    trip = get_object_or_404(Trips, id=id)

    if request.method == "GET":
        serializer = tripsSerializer(trip)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = tripsSerializer(trip, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        trip.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
