from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from cars.serializers import CarSerializer
from .models import Car


@api_view(["GET", "POST"])
def get_cars(request):
    if request.method == "GET":
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def car_detail(request, id):
    car = get_object_or_404(Car, id=id)

    if request.method == "GET":
        serializer = CarSerializer(car)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
