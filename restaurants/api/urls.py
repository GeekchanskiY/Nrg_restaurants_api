"""restaurants URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import get_all_restaurants, get_all_restaurant_dishes, get_dishes_category, post_restaurant_review,\
    get_restaurant_reviews, get_restaurant_dish_sets, get_all_news

urlpatterns = [
    path('restaurants/all', get_all_restaurants, name="get_all_restaurants"),
    path('dishes/restaurant/<int:pk>', get_all_restaurant_dishes, name="get_all_restaurant dishes"),
    path('dishes/category/<int:pk>', get_dishes_category, name="get_dishes_category"),
    path('dishes/dish_sets/<int:pk>', get_restaurant_dish_sets, name="get_dish_sets"),
    path('reviews/create', post_restaurant_review, name="create_restaurant_review"),
    path('reviews/get/<int:pk>', get_restaurant_reviews, name="get_restaurant_reviews"),
    path('news/all', get_all_news, name="get_all_news")
]
