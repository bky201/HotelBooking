# Generated by Django 3.2 on 2023-07-23 16:47

from django.db import migrations
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('roombooking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='description',
            field=djrichtextfield.models.RichTextField(max_length=10000),
        ),
    ]
