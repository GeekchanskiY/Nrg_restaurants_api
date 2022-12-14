from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from main.models import Restaurant, Dish, DishesCategory, DishSet, RestaurantImageCategory, RestaurantImage, Review,\
    News


class RestaurantImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RestaurantImage
        fields = ('id', 'image', 'name')
        read_only_fields = ('id', 'image', 'name')


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
        fields = ('id', 'name', 'front_end_key', 'restaurantimagecategory_set')
        read_only_fields = ('id', 'name', 'front_end_key', 'restaurantimagecategory_set')


class LightRestaurantSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'front_end_key')
        read_only_fields = ('id', 'name', 'front_end_key')


class DishSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Dish
        fields = ('id', 'name_ru', 'name_en', 'price', 'description_ru', 'description_en')


class DishesCategorySerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    dishes = DishSerializer(many=True)

    class Meta:
        model = DishesCategory
        fields = ('id', 'name_ru', 'name_en', 'image', 'dishes')


class DishSetSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    dishes = DishSerializer(many=True)

    class Meta:
        model = DishSet
        fields = ('id', 'name_ru', 'name_en', 'image', 'dishes')


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    time = serializers.DateTimeField(read_only=True)
    restaurant_front_end_key = serializers.PrimaryKeyRelatedField(queryset=Restaurant.objects.all(),
                                                                  source='restaurant.front_end_key')

    class Meta:
        model = Review
        fields = ('id', 'customer_email', 'customer_name', 'time', 'customer_rating_1', 'customer_rating_2',
                  'customer_rating_3', 'restaurant_front_end_key', 'customer_text')

    def create(self, validated_data):
        restaurant = validated_data.pop("restaurant")
        restaurant_front_end_key = restaurant["front_end_key"].front_end_key
        try:
            restaurant = Restaurant.objects.get(front_end_key=restaurant_front_end_key)
        except ObjectDoesNotExist:
            raise ValidationError(detail="Invalid restaurant front_end_key")

        review = Review(restaurant=restaurant, **validated_data)
        review.save()
        return review


class RestaurantDishSerializer(serializers.HyperlinkedModelSerializer):
    dishescategory_set = DishesCategorySerializer(many=True)

    class Meta:
        model = Restaurant
        fields = ('dishescategory_set',)
        read_only_fields = ('dishescategory_set',)


class NewsSerializer(serializers.HyperlinkedModelSerializer):
    restaurant = LightRestaurantSerializer()

    class Meta:
        model = News
        fields = ('id', 'article', 'time_posted', 'image', 'text', 'restaurant')
        read_only_fields = ['id']


        
