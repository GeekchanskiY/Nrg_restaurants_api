from django.shortcuts import render
from rest_framework import viewsets
from main.models import Restaurant
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .serializers import RestaurantSerializer

# Create your views here.


@swagger_auto_schema(methods=["get", "post"], responses={200: RestaurantSerializer(many=True)})
@api_view(['GET', 'POST'])
def test(request: Request):
    if request.method == "GET":
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        return Response(request.data, status=status.HTTP_200_OK)
