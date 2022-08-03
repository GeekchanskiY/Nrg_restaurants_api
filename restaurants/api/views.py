from django.shortcuts import render
from rest_framework import viewsets
from main.models import Restaurant, Dish, DishesCategory
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .serializers import RestaurantSerializer, DishSerializer, DishesCategorySerializer
from django.db import connection, reset_queries

# Create your views here.


@swagger_auto_schema(method="get", responses={200: RestaurantSerializer(many=True)})
@api_view(['GET'])
def get_all_restaurants(request: Request):
    restaurants = Restaurant.objects.all()
    serializer = RestaurantSerializer(restaurants, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema(method="get", responses={200: RestaurantSerializer(many=True)})
@api_view(['GET'])
def get_all_restaurants_categories(request: Request):
    restaurants = Restaurant.objects.all()
    serializer = RestaurantSerializer(restaurants, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema(method="get", responses={200: DishSerializer(many=True)})
@api_view(['GET'])
def get_all_restaurant_dishes(request: Request, pk: int):
    dishes = Dish.objects.filter(restaurant__id=pk)
    
    serializer = DishSerializer(dishes, many=True)
    return Response({"dishes": serializer.data},
                    status=status.HTTP_200_OK)


@swagger_auto_schema(method="get", responses={200: DishesCategorySerializer()})
@api_view(['GET'])
def get_dishes_category(request: Request, pk: int):
    dishes_category = DishesCategory.objects.get(id=pk)

    serializer = DishesCategorySerializer(dishes_category)
    return Response({"dishes": serializer.data},
                    status=status.HTTP_200_OK)

