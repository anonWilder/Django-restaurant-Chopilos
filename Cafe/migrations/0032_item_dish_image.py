# Generated by Django 3.2.18 on 2023-07-16 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cafe', '0031_delete_gallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='dish_image',
            field=models.ImageField(default='/static/images/icons/shef.png', upload_to='dish_image/'),
        ),
    ]
