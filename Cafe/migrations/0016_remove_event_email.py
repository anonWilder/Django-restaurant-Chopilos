# Generated by Django 3.2.18 on 2023-04-17 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cafe', '0015_event_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='email',
        ),
    ]
