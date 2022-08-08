from django.db import models
from django.utils.html import mark_safe
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


class Restaurant(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name="Название", unique=True)
    front_end_key = models.IntegerField(unique=True, null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return f"{self.id} - {self.name}"

    class Meta:
        verbose_name = "Ресторан"
        verbose_name_plural = "Рестораны"


class News(models.Model):
    id: models.AutoField = models.AutoField(primary_key=True)
    article = models.CharField(max_length=255)
    time_posted = models.DateTimeField(default=datetime.now)
    image = models.ImageField(upload_to="images/news/")
    text = models.TextField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=True)

    objects = models.Manager()

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


class Dish(models.Model):
    id = models.AutoField(primary_key=True)
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    price = models.FloatField()
    description_ru = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        if self.name_ru is not None:
            return f"{self.name_ru} - {str(self.restaurant)}"
        else:
            return "None"

    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"


class DishesCategory(models.Model):
    id = models.AutoField(primary_key=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/dishes_categories/", null=True, blank=True)
    dishes = models.ManyToManyField(Dish)

    objects = models.Manager()

    def __str__(self):
        if self.name_ru is not None:
            return self.name_ru
        else:
            return "None"

    class Meta:
        verbose_name = "Категория блюд"
        verbose_name_plural = "Категории блюд"


class DishSet(models.Model):
    id = models.AutoField(primary_key=True)
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    dishes = models.ManyToManyField(Dish)
    image = models.ImageField(upload_to="images/dish_sets/")

    objects = models.Manager()

    def image_tag(self):
        return mark_safe(f'<img src="{self.image.url}" width="70" height="70" />')

    image_tag.short_description = 'Image'

    def __str__(self):
        if self.name_ru is not None:
            return self.name_ru
        else:
            return "None"

    class Meta:
        verbose_name = "Набор"
        verbose_name_plural = "Наборы"
    

class RestaurantImageCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория изображений"
        verbose_name_plural = "Категории изображений"


class RestaurantImage(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(RestaurantImageCategory, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to="images/restaurants/")
    default = models.BooleanField(default=False)

    objects = models.Manager()

    def image_tag(self):
        return mark_safe(f'<img src="{self.image.url}" width="70" height="70" />')

    image_tag.short_description = 'Image'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Изображение ресторана"
        verbose_name_plural = "Изображения ресторана"


class Review(models.Model):
    id = models.AutoField(primary_key=True)
    customer_email = models.EmailField(blank=True, null=True)
    customer_name = models.CharField(max_length=255, blank=True, null=True)
    customer_rating_1 = models.IntegerField(default=10, validators=[MaxValueValidator(10), MinValueValidator(1)])
    customer_rating_2 = models.IntegerField(default=10, validators=[MaxValueValidator(10), MinValueValidator(1)])
    customer_rating_3 = models.IntegerField(default=10, validators=[MaxValueValidator(10), MinValueValidator(1)])
    time = models.DateTimeField(default=datetime.now, blank=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    customer_text = models.TextField(null=True, blank=True)
    is_shown = models.BooleanField(default=False)

    objects = models.Manager()

    def __str__(self):
        return self.customer_email

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


class AdminUser(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    email = None
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Администратор"
        verbose_name_plural = "Администраторы"
