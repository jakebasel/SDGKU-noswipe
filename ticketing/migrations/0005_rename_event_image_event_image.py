# Generated by Django 3.2.6 on 2021-10-13 01:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0004_event_event_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='event_image',
            new_name='image',
        ),
    ]
