# Generated by Django 3.2.18 on 2023-07-16 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomePage', '0007_auto_20230716_1258'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('count', models.CharField(max_length=1000)),
            ],
        ),
    ]