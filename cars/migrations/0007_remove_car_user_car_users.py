# Generated by Django 5.1.2 on 2024-11-09 23:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0006_alter_car_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='user',
        ),
        migrations.AddField(
            model_name='car',
            name='users',
            field=models.ManyToManyField(related_name='cars', to=settings.AUTH_USER_MODEL),
        ),
    ]
