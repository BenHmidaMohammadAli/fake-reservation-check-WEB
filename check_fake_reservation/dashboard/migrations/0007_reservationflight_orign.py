# Generated by Django 4.1.7 on 2023-05-06 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_flight_route_flight_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservationflight',
            name='orign',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]