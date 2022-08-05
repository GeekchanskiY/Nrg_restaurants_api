from django.shortcuts import render
from rest_framework import viewsets
from main.models import Restaurant, Dish, DishesCategory, Review, DishSet, News
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.exceptions import ValidationError
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .serializers import RestaurantSerializer, DishSerializer, DishesCategorySerializer, ReviewSerializer,\
    DishSetSerializer, NewsSerializer

from django.db import connection, reset_queries

# Create your views here.


@swagger_auto_schema(method="get", responses={200: RestaurantSerializer(many=True)})
@api_view(['GET'])
def get_all_restaurants(request: Request):
    restaurants = Restaurant.objects.all()
    serializer = RestaurantSerializer(restaurants, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema(method="get", responses={200: NewsSerializer(many=True)})
@api_view(['GET'])
def get_all_news(requests: Request):
    news = News.objects.all()
    serializer = NewsSerializer(news, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema(method="get", responses={200: NewsSerializer(many=True)})
@api_view(['GET'])
def get_all_news_exclude(requests: Request, pk: int):
    news = News.objects.exclude(id=pk)
    serializer = NewsSerializer(news, many=True)
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
    return Response(serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema(method="get", responses={200: DishesCategorySerializer()})
@api_view(['GET'])
def get_dishes_category(request: Request, pk: int):
    dishes_category = DishesCategory.objects.get(id=pk)

    serializer = DishesCategorySerializer(dishes_category)
    return Response(serializer.data,
                    status=status.HTTP_200_OK)


@swagger_auto_schema(method="post", request_body=ReviewSerializer(), responses={
    201: ReviewSerializer(),
    400: openapi.Response('Validation error {error: str, data: dict}')
})
@api_view(['POST'])
def post_restaurant_review(request: Request):
    try:
        reviews_serializer = ReviewSerializer(data=request.data)
        if reviews_serializer.is_valid(raise_exception=True):
            review = reviews_serializer.save()
        return Response(reviews_serializer.data, status=status.HTTP_201_CREATED)
    except ValidationError as e:
        return Response(dict(error=str(e), data=request.data), status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method="get", responses={200: ReviewSerializer(many=True)})
@api_view(['GET'])
def get_restaurant_reviews(request: Request, pk: int):
    reviews = Review.objects.filter(restaurant__id=pk)
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema(method="get", responses={200: DishSetSerializer(many=True)})
@api_view(['GET'])
def get_restaurant_dish_sets(request: Request, pk: int):
    dish_sets = DishSet.objects.filter(restaurant__id=pk)
    serializer = DishSetSerializer(dish_sets, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

