# Generated by Django 5.0.4 on 2024-04-28 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_remove_cart_courses'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
