from abc import ABC

from rest_framework import serializers
from main.models import Restaurant, Dish, DishesCategory


class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Restaurant
        fields = ('id', 'name')


class DishSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    category_id = serializers.CharField(read_only=True, source='category.id')

    class Meta:
        model = Dish
        fields = ('id', 'name', 'price', 'description', 'category_id')


class DishesCategorySerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = DishesCategory
        fields = ('id', 'name', 'image')
