# Generated by Django 4.2.5 on 2023-10-01 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='watchAgain',
            field=models.BooleanField(default=False),
        ),
    ]
