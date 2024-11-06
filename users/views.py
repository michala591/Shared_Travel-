from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import userSerializer
from .models import User


@api_view(["GET", "POST"])
def get_users(request):
    if request.method == "GET":
        users = User.objects.all()
        serializer = userSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = userSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def user_detail(request, id):
    user = get_object_or_404(User, id=id)

    if request.method == "GET":
        serializer = userSerializer(user)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = userSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
