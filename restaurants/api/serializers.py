from rest_framework import serializers
from main.models import Restaurant, Dish, DishesCategory, DishSet, RestaurantImageCategory, RestaurantImage, Review


class RestaurantImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RestaurantImage
        fields = ('image', 'name')


class RestaurantImageCategorySerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    restaurantimage_set = RestaurantImageSerializer(many=True)

    class Meta:
        model = RestaurantImageCategory
        fields = ('id', 'name', 'restaurantimage_set')


class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    restaurantimagecategory_set = RestaurantImageCategorySerializer(many=True)

    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'restaurantimagecategory_set')


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


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    time = serializers.DateTimeField(read_only=True)
    restaurant_id = serializers.PrimaryKeyRelatedField(queryset=Restaurant.objects.all(), source='restaurant.id')

    class Meta:
        model = Review
        fields = ('id', 'customer_email', 'customer_name', 'time', 'customer_rating', 'restaurant_id', 'customer_text')
