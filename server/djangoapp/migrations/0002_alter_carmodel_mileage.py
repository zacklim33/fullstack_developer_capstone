# Generated by Django 5.1.4 on 2025-01-12 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='mileage',
            field=models.IntegerField(default=10000),
        ),
    ]
