# Generated by Django 3.1.4 on 2020-12-18 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marcial', '0002_auto_20201218_1616'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aeronave_pasajero',
            name='name',
        ),
    ]
