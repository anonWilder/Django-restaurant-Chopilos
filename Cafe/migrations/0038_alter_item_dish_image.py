# Generated by Django 3.2.18 on 2023-07-16 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cafe', '0037_alter_item_dish_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='dish_image',
            field=models.ImageField(upload_to='dish_image/'),
        ),
    ]
