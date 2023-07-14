# Generated by Django 3.2.18 on 2023-07-14 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cafe', '0024_auto_20230714_0024'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='special_images/')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]