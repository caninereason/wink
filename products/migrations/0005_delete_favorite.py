# Generated by Django 3.2.3 on 2023-10-18 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20231018_1540'),
        ('products', '0004_auto_20231018_1540'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Favorite',
        ),
    ]
