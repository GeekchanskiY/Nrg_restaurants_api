from django.db import models
from django.utils.html import mark_safe
from django.conf import settings

# Create your models here.


class Restaurant(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name="Название", unique=True)


class DishesCategory(models.Model):
    id = models.AutoField(primary_key=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/dishes_categories/", null=True, blank=True)


class Dish(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    category = models.ForeignKey(DishesCategory, on_delete=models.CASCADE)


class DishSet(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    dishes = models.ManyToManyField(Dish)
    image = models.ImageField(upload_to="images/dish_sets/")

    def image_tag(self):
        return mark_safe(f'<img src="{self.image.url}" width="70" height="70" />')

    image_tag.short_description = 'Image'
    

class RestaurantImageCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)


class RestaurantImage(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    category = models.ForeignKey(RestaurantImageCategory, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to="images/restaurants/")
    default = models.BooleanField(default=False)

    def image_tag(self):
        return mark_safe(f'<img src="{self.image.url}" width="70" height="70" />')

    image_tag.short_description = 'Image'


