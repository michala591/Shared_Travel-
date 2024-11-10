from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsDriverUser
from .serializers import SearchTripsSerializer, UserSerializer, tripsSerializer
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
@permission_classes([IsAuthenticated, IsDriverUser])
def trip_detail(request, id):
    trip = get_object_or_404(Trips, id=id)

    if trip.car.user != request.user:
        return Response(
            {"error": "You can only access your own trips."},
            status=status.HTTP_403_FORBIDDEN,
        )
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


@api_view(["GET"])
@permission_classes([IsAuthenticated, IsDriverUser])
def get_passengers(request, id):
    trip = get_object_or_404(Trips, id=id)
    passengers = trip.users.all()
    serializer = UserSerializer(passengers, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_active_trips(request):
    if request.method == "GET":
        trips = Trips.objects.filter(users__user_type="DR", users__is_enabled=True)
        serializer = tripsSerializer(trips, many=True)
        return Response(serializer.data)


@api_view(["GET"])
def search_trips(request):
    letter = request.query_params.get("letter", None)

    if letter:
        trips = Trips.objects.filter(
            origin_station__city__startswith=letter
        ) | Trips.objects.filter(origin_station__zone__startswith=letter)

        trips = [trip for trip in trips if trip.has_available_seats()]

        serializer = SearchTripsSerializer(trips, many=True)
        return Response(serializer.data)

    return Response(
        {"detail": "Letter parameter is required."}, status=status.HTTP_400_BAD_REQUEST
    )


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def invite_to_trip(request, id):
    trip = get_object_or_404(Trips, id=id)
    if request.user in trip.users.all():
        return Response(
            {"error": "You are already part of this trip."},
            status=status.HTTP_400_BAD_REQUEST,
        )
    if Trips.objects.filter(users=request.user):
        return Response(
            {"error": "You are already part of trips."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if not trip.has_available_seats():
        return Response(
            {"error": "No available seats on this trip."},
            status=status.HTTP_400_BAD_REQUEST,
        )
    trip.users.add(request.user)
    return Response(
        {
            "status": f"You have been successfully added to the trip from {trip.origin_station} to {trip.destination_station}."
        },
        status=status.HTTP_200_OK,
    )
