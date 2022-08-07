from django.contrib import admin
from .models import Restaurant, Dish, DishSet, DishesCategory, RestaurantImage, RestaurantImageCategory, Review, \
    AdminUser, News
from django.core.exceptions import ValidationError

# Register your models here.


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'front_end_key')
    fields = ['name', 'front_end_key']
    search_fields = ['name']


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('name_ru', 'name_en', 'price')
    fields = ('name_ru', 'name_en', 'price', 'description', 'category', 'restaurant')
    search_fields = ['name_ru', 'name_en']

    def get_queryset(self, request):
        """
        Return a QuerySet of all model instances that can be edited by the
        admin site. This is used by changelist_view.
        """
        qs = self.model._default_manager.get_queryset()
        ordering = self.get_ordering(request)
        if request.user.is_superuser:
            if ordering:
                qs = qs.order_by(*ordering)
            return qs
        qs = qs.filter(restaurant__id=request.user.restaurant.id)
        return qs

    def save_form(self, request, form, change):
        """
        Given a ModelForm return an unsaved instance. ``change`` is True if
        the object is being changed, and False if it's being added.
        """
        return form.save(commit=False)

    def save_model(self, request, obj, form, change):
        """
        Given a model instance save it to the database.
        """
        if request.user.is_superuser or obj.restaurant.id == request.user.restaurant.id:
            obj.save()

    def delete_model(self, request, obj):
        """
        Given a model instance delete it from the database.
        """
        if request.user.is_superuser or obj.restaurant.id == request.user.restaurant.id:
            obj.delete()


@admin.register(DishSet)
class DishSetAdmin(admin.ModelAdmin):
    list_display = ('name_ru', 'name_en', 'image_tag')
    fields = ('name_ru', 'name_en', 'restaurant', 'dishes', 'image', 'image_tag')
    readonly_fields = ['image_tag']
    search_fields = ['name_ru', 'name_en']


@admin.register(DishesCategory)
class DishesCategoryAdmin(admin.ModelAdmin):
    list_display = ('name_ru', 'name_en')
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
    list_display = ('customer_name', 'customer_rating_1', 'customer_rating_2',
                    'customer_rating_3', 'is_shown')
    fields = ('customer_email', 'customer_name', 'customer_rating_1', 'customer_rating_2',
              'customer_rating_3', 'time', 'restaurant', 'is_shown')
    readonly_fields = ('customer_email', 'customer_name', 'customer_rating_1', 'customer_rating_2',
                       'customer_rating_3', 'time', 'restaurant', 'is_shown')


class RestaurantInline(admin.TabularInline):
    model = Restaurant


@admin.register(AdminUser)
class AdminUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'restaurant')
    fields = ('username', 'restaurant', 'is_staff', 'is_active', 'user_permissions')
    readonly_fields = ('id', 'username')


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('article', 'time_posted')
    fields = ('article', 'time_posted', 'image', 'text', 'restaurant')
    
