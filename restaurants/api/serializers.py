from abc import ABC

from rest_framework import serializers
from main.models import Restaurant


class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Restaurant
        fields = ('id', 'name')
    