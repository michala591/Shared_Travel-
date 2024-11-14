# Generated by Django 5.1.2 on 2024-11-10 00:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0002_remove_trips_user_trips_car'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='trips',
            name='users',
            field=models.ManyToManyField(related_name='cars', to=settings.AUTH_USER_MODEL),
        ),
    ]