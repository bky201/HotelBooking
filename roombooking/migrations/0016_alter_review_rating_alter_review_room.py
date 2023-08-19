# Generated by Django 4.2.3 on 2023-08-19 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("roombooking", "0015_alter_review_rating"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="rating",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="review",
            name="room",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="roombooking.room"
            ),
        ),
    ]
