# Generated by Django 3.2.3 on 2023-10-18 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20231018_1540'),
        ('profiles', '0002_userprofile_favorites'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='favorites',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='favourite_products',
            field=models.ManyToManyField(blank=True, related_name='favourite_by_users', to='products.Product'),
        ),
    ]
