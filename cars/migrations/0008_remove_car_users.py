# Generated by Django 5.1.2 on 2024-11-10 00:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0007_remove_car_user_car_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='users',
        ),
    ]