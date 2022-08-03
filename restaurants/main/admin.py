from django.contrib import admin
from .models import Restaurant

# Register your models here.


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    fields = ('name')
    search_fields = ['name']
    
