from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import locationsSerializer
from .models import Locations


@api_view(["GET", "POST"])
def get_locations(request):
    if request.method == "GET":
        locations = Locations.objects.all()
        serializer = locationsSerializer(locations, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = locationsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def location_detail(request, id):
    location = get_object_or_404(Locations, id=id)

    if request.method == "GET":
        serializer = locationsSerializer(location)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = locationsSerializer(location, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        location.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
