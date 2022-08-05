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


class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'article', 'time_posted', 'image', 'text')


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
        fields = ('id', 'name', 'front_end_key','restaurantimagecategory_set')
        read_only_fields = ('id', 'name', 'front_end_key', 'restaurantimagecategory_set')


class DishSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Dish
        fields = ('id', 'name_ru', 'name_en', 'price', 'description')


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
    restaurant_id = serializers.PrimaryKeyRelatedField(queryset=Restaurant.objects.all(),
                                                       source='restaurant.id')

    class Meta:
        model = Review
        fields = ('id', 'customer_email', 'customer_name', 'time', 'customer_rating_1', 'customer_rating_2',
                  'customer_rating_3', 'restaurant_id', 'customer_text')

    def create(self, validated_data):
        restaurant = validated_data.pop("restaurant")
        restaurant_id = restaurant["id"].id
        try:
            restaurant = Restaurant.objects.get(id=restaurant_id)
        except ObjectDoesNotExist:
            raise ValidationError(detail="Invalid restaurant id")

        review = Review(restaurant=restaurant, **validated_data)
        review.save()
        return review


class RestaurantDishSerializer(serializers.HyperlinkedModelSerializer):
    dishescategory_set = DishesCategorySerializer(many=True)
    dishset_set = DishSetSerializer(many=True)

    class Meta:
        model = Restaurant
        fields = ('dishes_set', 'dishes_sets')
        read_only_fields = ('dishescategory_set', 'dishset_set')


        
