# Generated by Django 3.2.6 on 2021-10-20 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0013_auto_20211019_1922'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='ticket_holder',
            new_name='ticket_holder_email',
        ),
        migrations.AddField(
            model_name='ticket',
            name='ticket_holder_first_name',
            field=models.CharField(default=10, max_length=55),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticket',
            name='ticket_holder_last_name',
            field=models.CharField(default=10, max_length=55),
            preserve_default=False,
        ),
    ]