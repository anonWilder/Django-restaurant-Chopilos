# Generated by Django 3.2.18 on 2023-07-16 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cafe', '0032_item_dish_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='image',
        ),
    ]
