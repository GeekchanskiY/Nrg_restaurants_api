from django.contrib import admin
from .models import Restaurant, Dish, DishSet, DishesCategory, RestaurantImage, RestaurantImageCategory

# Register your models here.


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    fields = ['name']
    search_fields = ['name']


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    fields = ('name', 'price', 'description', 'category', 'restaurant')
    search_fields = ['name']


@admin.register(DishSet)
class DishSetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image_tag')
    fields = ('name', 'restaurant', 'dishes', 'image', 'image_tag')
    readonly_fields = ['image_tag']


@admin.register(DishesCategory)
class DishesCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    fields = ('restaurant', 'name', 'image')


@admin.register(RestaurantImage)
class RestaurantImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_tag')
    fields = ('name', 'image', 'image_tag', 'restaurant', 'category', 'default')
    readonly_fields = ['image_tag']


@admin.register(RestaurantImageCategory)
class RestaurantImageCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    fields = ('name', 'restaurant')
    
