# Generated by Django 4.0.6 on 2022-08-07 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_restaurant_front_end_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='restaurant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.restaurant'),
        ),
    ]