# Generated by Django 3.2.6 on 2021-10-29 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0020_rename_current_attendee_event_current_attendee_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='remaining_capacity',
            field=models.BigIntegerField(default=45),
            preserve_default=False,
        ),
    ]