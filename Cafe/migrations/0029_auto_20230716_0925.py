# Generated by Django 3.2.18 on 2023-07-16 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cafe', '0028_contactinfo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ContactInfo',
        ),
        migrations.DeleteModel(
            name='OfferSection',
        ),
        migrations.DeleteModel(
            name='SlideshowItem',
        ),
        migrations.DeleteModel(
            name='SpecialSection',
        ),
    ]