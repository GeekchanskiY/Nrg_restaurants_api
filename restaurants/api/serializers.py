from abc import ABC

from rest_framework import serializers
from main.models import Restaurant, Dish, DishesCategory, DishSet, RestaurantImageCategory, RestaurantImage


class RestaurantImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RestaurantImage
        fields = ('image', 'name')


class RestaurantImageCategorySerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    images_set = RestaurantImageSerializer(many=True)

    class Meta:
        model = RestaurantImageCategory
        fields = ('id', 'name', 'images_set')


class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    image_categories_set = RestaurantImageCategorySerializer(many=True)

    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'image_categories_set')


class DishSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    category_id = serializers.CharField(read_only=True, source='category.id')

    class Meta:
        model = Dish
        fields = ('id', 'name_ru', 'name_en', 'price', 'description', 'category_id')


class DishesCategorySerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    dishes_set = DishSerializer(many=True)

    class Meta:
        model = DishesCategory
        fields = ('id', 'name_ru', 'name_en', 'image', 'dishes_set')


class DishSetSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    dishes_set = DishSerializer(many=True)

    class Meta:
        model = DishSet
        fields = ('id', 'name_ru', 'name_en', 'image', 'dishes_set')
