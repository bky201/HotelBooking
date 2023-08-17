# Generated by Django 4.2.3 on 2023-08-16 09:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("roombooking", "0005_remove_room_rating_review"),
    ]

    operations = [
        migrations.RenameField(
            model_name="review",
            old_name="created_on",
            new_name="created_at",
        ),
        migrations.RenameField(
            model_name="review",
            old_name="comment",
            new_name="review",
        ),
        migrations.AddField(
            model_name="review",
            name="status",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="review",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]