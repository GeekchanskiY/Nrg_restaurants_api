from django.contrib import admin
from .models import Restaurant, Dish, DishesCategory, RestaurantImage, RestaurantImageCategory, Review, \
    AdminUser, News
from django.core.exceptions import ValidationError
from hijack.contrib.admin import HijackUserAdminMixin
# Register your models here.


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'front_end_key')
    fields = ['name', 'front_end_key']
    search_fields = ['name']


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('name_ru', 'name_en', 'price')
    fields = ('name_ru', 'name_en', 'price', 'description_ru', 'description_en', 'restaurant')
    search_fields = ['name_ru', 'name_en']

    def get_queryset(self, request):
        qs = self.model._default_manager.get_queryset()
        ordering = self.get_ordering(request)
        if request.user.is_superuser:
            if ordering:
                qs = qs.order_by(*ordering)
            return qs
        qs = qs.filter(restaurant__id=request.user.restaurant.id)
        if ordering:
            qs = qs.order_by(*ordering)
        return qs

    def save_model(self, request, obj, form, change):
        if request.user.is_superuser or obj.restaurant.id == request.user.restaurant.id:
            obj.save()

    def delete_model(self, request, obj):
        if request.user.is_superuser or obj.restaurant.id == request.user.restaurant.id:
            obj.delete()

    def get_form(self, request, obj=None, **kwargs):
        form = super(DishAdmin, self).get_form(request, obj, **kwargs)
        if not request.user.is_superuser:
            form.base_fields['restaurant'].queryset = Restaurant.objects.filter(id=request.user.restaurant.id)
        return form


@admin.register(DishesCategory)
class DishesCategoryAdmin(admin.ModelAdmin):
    list_display = ('name_ru', 'name_en')
    fields = ('restaurant', 'name_ru', 'name_en', 'image', 'dishes', 'priority')
    search_fields = ('name_ru', 'name_en')
    filter_horizontal = ('dishes',)

    def get_queryset(self, request):
        qs = self.model._default_manager.get_queryset()
        ordering = self.get_ordering(request)

        if request.user.is_superuser:
            if ordering:
                qs = qs.order_by(*ordering)
            return qs

        qs = qs.filter(restaurant__id=request.user.restaurant.id)
        if ordering:
            qs = qs.order_by(*ordering)
        return qs

    def save_model(self, request, obj, form, change):
        if request.user.is_superuser or obj.restaurant.id == request.user.restaurant.id:
            obj.save()

    def delete_model(self, request, obj):
        if request.user.is_superuser or obj.restaurant.id == request.user.restaurant.id:
            obj.delete()

    def get_form(self, request, obj=None, **kwargs):
        form = super(DishesCategoryAdmin, self).get_form(request, obj, **kwargs)
        if not request.user.is_superuser:
            form.base_fields['restaurant'].queryset = Restaurant.objects.filter(id=request.user.restaurant.id)
            form.base_fields['dishes'].queryset = Dish.objects.filter(restaurant__id=request.user.restaurant.id)
        return form


@admin.register(RestaurantImage)
class RestaurantImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_tag')
    fields = ('name', 'image', 'image_tag', 'category', 'default')
    readonly_fields = ('image_tag', )

    def get_queryset(self, request):
        qs = self.model._default_manager.get_queryset()
        ordering = self.get_ordering(request)

        if request.user.is_superuser:
            if ordering:
                qs = qs.order_by(*ordering)
            return qs

        qs = qs.filter(category__restaurant__id=request.user.restaurant.id)
        if ordering:
            qs = qs.order_by(*ordering)
        return qs

    def save_model(self, request, obj, form, change):
        if request.user.is_superuser or obj.category.restaurant.id == request.user.restaurant.id:
            obj.save()

    def delete_model(self, request, obj):
        if request.user.is_superuser or obj.category.restaurant.id == request.user.restaurant.id:
            obj.delete()

    def get_form(self, request, obj=None, **kwargs):
        form = super(RestaurantImageAdmin, self).get_form(request, obj, **kwargs)
        if not request.user.is_superuser:
            form.base_fields['category'].queryset = RestaurantImageCategory.objects.filter(
                restaurant__id=request.user.restaurant.id
            )
        return form


@admin.register(RestaurantImageCategory)
class RestaurantImageCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fields = ('name', 'restaurant')

    def get_queryset(self, request):
        qs = self.model._default_manager.get_queryset()
        ordering = self.get_ordering(request)

        if request.user.is_superuser:
            if ordering:
                qs = qs.order_by(*ordering)
            return qs

        qs = qs.filter(restaurant__id=request.user.restaurant.id)
        if ordering:
            qs = qs.order_by(*ordering)
        return qs

    def save_model(self, request, obj, form, change):
        if request.user.is_superuser or obj.restaurant.id == request.user.restaurant.id:
            obj.save()

    def delete_model(self, request, obj):
        if request.user.is_superuser or obj.restaurant.id == request.user.restaurant.id:
            obj.delete()

    def get_form(self, request, obj=None, **kwargs):
        form = super(RestaurantImageCategoryAdmin, self).get_form(request, obj, **kwargs)
        if not request.user.is_superuser:
            form.base_fields['restaurant'].queryset = Restaurant.objects.filter(id=request.user.restaurant.id)
        return form


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_rating_1', 'customer_rating_2',
                    'customer_rating_3', 'time')
    fields = ('customer_email', 'customer_name', 'customer_rating_1', 'customer_rating_2',
              'customer_rating_3', 'time', 'restaurant', 'is_shown')
    readonly_fields = ('customer_email', 'customer_name', 'customer_rating_1', 'customer_rating_2',
                       'customer_rating_3', 'time', 'restaurant', 'is_shown')

    def get_queryset(self, request):
        qs = self.model._default_manager.get_queryset()
        ordering = self.get_ordering(request)

        if request.user.is_superuser:
            if ordering:
                qs = qs.order_by(*ordering)
            return qs

        qs = qs.filter(restaurant__id=request.user.restaurant.id)
        if ordering:
            qs = qs.order_by(*ordering)
        return qs

    def save_model(self, request, obj, form, change):
        if request.user.is_superuser or obj.restaurant.id == request.user.restaurant.id:
            obj.save()

    def delete_model(self, request, obj):
        if request.user.is_superuser or obj.restaurant.id == request.user.restaurant.id:
            obj.delete()

    def get_form(self, request, obj=None, **kwargs):
        form = super(ReviewAdmin, self).get_form(request, obj, **kwargs)
        return form


@admin.register(AdminUser)
class AdminUserAdmin(HijackUserAdminMixin, admin.ModelAdmin):
    readonly_fields = ('id', 'username')
    filter_horizontal = ('user_permissions',)

    def get_hijack_user(self, obj):
        return obj



@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('article', 'time_posted')
    fields = ('article', 'time_posted', 'image', 'text', 'restaurant')

    def get_queryset(self, request):
        qs = self.model._default_manager.get_queryset()
        ordering = self.get_ordering(request)

        if request.user.is_superuser:
            if ordering:
                qs = qs.order_by(*ordering)
            return qs

        qs = qs.filter(restaurant__id=request.user.restaurant.id)
        if ordering:
            qs = qs.order_by(*ordering)
        return qs

    def save_model(self, request, obj, form, change):
        if request.user.is_superuser or obj.restaurant.id == request.user.restaurant.id:
            obj.save()

    def delete_model(self, request, obj):
        if request.user.is_superuser or obj.restaurant.id == request.user.restaurant.id:
            obj.delete()

    def get_form(self, request, obj=None, **kwargs):
        form = super(NewsAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['restaurant'].queryset = Restaurant.objects.filter(id=request.user.restaurant.id)
        return form
    
