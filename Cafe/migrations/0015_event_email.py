# Generated by Django 3.2.18 on 2023-04-17 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cafe', '0014_remove_event_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=400, null=True),
        ),
    ]
