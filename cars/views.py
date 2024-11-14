from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from cars.serializers import CarIdSerializer, CarSerializer
from users.permissions import IsDriverUser
from .models import Car


# @api_view(["GET", "POST"])
# def get_cars(request):
#     if request.method == "GET":
#         print("Received request for cars")
#         cars = Car.objects.all()
#         # cars = Car.objects.filter(user=request.user)
#         serializer = CarSerializer(cars, many=True)
#         return Response(serializer.data)

# elif request.method == "POST":
#     serializer = CarSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "POST", "PUT", "DELETE"])
@permission_classes([IsAuthenticated, IsDriverUser])
def car_detail(request):

    if request.method == "GET":
        car = get_object_or_404(Car, user=request.user)
        serializer = CarSerializer(car)
        return Response(serializer.data)

    elif request.method == "POST":
        try:
            car = Car.objects.create(
                license_plate=request.data["license_plate"],
                model=request.data["model"],
                max_capacity=request.data["max_capacity"],
                user=request.user,
            )

            car.save()

            return Response(
                {"message": "Car added successfully."},
                status=status.HTTP_201_CREATED,
            )
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PUT":
        car = get_object_or_404(Car, user=request.user)
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        car = get_object_or_404(Car, user=request.user)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
