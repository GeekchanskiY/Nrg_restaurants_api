from django.contrib import admin
from .models import Restaurant, Dish, DishSet, DishesCategory, RestaurantImage, RestaurantImageCategory, Review, \
    AdminUser
from django.core.exceptions import ValidationError

# Register your models here.


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    fields = ['name']
    search_fields = ['name']


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_ru', 'name_en', 'price')
    fields = ('name_ru', 'name_en', 'price', 'description', 'category', 'restaurant')
    search_fields = ['name_ru', 'name_en']

    """def get_object(self, request, object_id, from_field=None):
        queryset = self.get_queryset(request)
        model = queryset.model
        field = (
            model._meta.pk if from_field is None else model._meta.get_field(from_field)
        )
        try:
            object_id = field.to_python(object_id)
            return queryset.get(**{field.name: object_id})
        except (model.DoesNotExist, ValidationError, ValueError):
            return None"""


@admin.register(DishSet)
class DishSetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_ru', 'name_en', 'image_tag')
    fields = ('name_ru', 'name_en', 'restaurant', 'dishes', 'image', 'image_tag')
    readonly_fields = ['image_tag']
    search_fields = ['name_ru', 'name_en']


@admin.register(DishesCategory)
class DishesCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_ru', 'name_en')
    fields = ('restaurant', 'name_ru', 'name_en', 'image')
    search_fields = ['name_ru', 'name_en']


@admin.register(RestaurantImage)
class RestaurantImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_tag')
    fields = ('name', 'image', 'image_tag', 'restaurant', 'category', 'default')
    readonly_fields = ['image_tag']


@admin.register(RestaurantImageCategory)
class RestaurantImageCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    fields = ('name', 'restaurant')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_rating_1', 'customer_rating_2',
                    'customer_rating_3', 'is_shown')
    fields = ('customer_email', 'customer_name', 'customer_rating_1', 'customer_rating_2',
              'customer_rating_3', 'time', 'restaurant', 'is_shown')
    readonly_fields = ['time']


class RestaurantInline(admin.TabularInline):
    model = Restaurant


@admin.register(AdminUser)
class AdminUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'restaurant')
    fields = ('id', 'username', 'password', 'restaurant')
    readonly_fields = ['id']
    
