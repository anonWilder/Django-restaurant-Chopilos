# Generated by Django 3.2.18 on 2023-07-16 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotdeal',
            name='instruction',
        ),
        migrations.AlterField(
            model_name='hotdeal',
            name='offer_end_period',
            field=models.CharField(max_length=8),
        ),
    ]
