# Generated by Django 3.2.6 on 2021-10-13 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0007_alter_event_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(default='null', upload_to='static/images/'),
        ),
    ]