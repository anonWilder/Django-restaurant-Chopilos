# Generated by Django 3.2.18 on 2023-07-13 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cafe', '0020_alter_item_bar_menu_listed'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfferSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtitle', models.CharField(max_length=100)),
                ('pattern_image', models.ImageField(upload_to='Index_offer_section/')),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
            ],
        ),
    ]