# Generated by Django 5.1.2 on 2024-11-05 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_plate', models.CharField(max_length=8, unique=True)),
                ('model', models.CharField(max_length=50)),
                ('max_capacity', models.IntegerField(default=5)),
            ],
        ),
    ]
