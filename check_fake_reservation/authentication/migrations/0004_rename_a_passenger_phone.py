# Generated by Django 4.1.7 on 2023-04-09 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_remove_passenger_phone_passenger_a'),
    ]

    operations = [
        migrations.RenameField(
            model_name='passenger',
            old_name='a',
            new_name='phone',
        ),
    ]
