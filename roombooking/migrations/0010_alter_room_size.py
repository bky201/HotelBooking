# Generated by Django 4.2.3 on 2023-08-21 16:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("roombooking", "0009_rename_created_date_booking_created_on"),
    ]

    operations = [
        migrations.AlterField(
            model_name="room",
            name="size",
            field=models.IntegerField(default=30, max_length=60),
        ),
    ]
