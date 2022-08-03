# Generated by Django 4.0.6 on 2022-08-03 11:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_restaurantimagecategory_restaurantimage_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('customer_name', models.CharField(max_length=255)),
                ('customer_rating', models.IntegerField(default=10, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('time', models.DateTimeField(auto_now=True)),
                ('is_shown', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterModelOptions(
            name='dish',
            options={'verbose_name': 'Блюдо', 'verbose_name_plural': 'Блюда'},
        ),
        migrations.AlterModelOptions(
            name='dishescategory',
            options={'verbose_name': 'Категория блюд', 'verbose_name_plural': 'Категории блюд'},
        ),
        migrations.AlterModelOptions(
            name='dishset',
            options={'verbose_name': 'Набор', 'verbose_name_plural': 'Наборы'},
        ),
        migrations.AlterModelOptions(
            name='restaurant',
            options={'verbose_name': 'Ресторан', 'verbose_name_plural': 'Рестораны'},
        ),
        migrations.AlterModelOptions(
            name='restaurantimage',
            options={'verbose_name': 'Изображение ресторана', 'verbose_name_plural': 'Изображения ресторана'},
        ),
        migrations.AlterModelOptions(
            name='restaurantimagecategory',
            options={'verbose_name': 'Категория изображений', 'verbose_name_plural': 'Категории изображений'},
        ),
        migrations.RemoveField(
            model_name='dish',
            name='name',
        ),
        migrations.RemoveField(
            model_name='dishescategory',
            name='name',
        ),
        migrations.RemoveField(
            model_name='dishset',
            name='name',
        ),
        migrations.AddField(
            model_name='dish',
            name='name_en',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='dish',
            name='name_ru',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='dishescategory',
            name='name_en',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='dishescategory',
            name='name_ru',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='dishset',
            name='name_en',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='dishset',
            name='name_ru',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]