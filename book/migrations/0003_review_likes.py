# Generated by Django 4.2.6 on 2023-10-06 07:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("book", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="review",
            name="likes",
            field=models.ManyToManyField(
                blank=True, related_name="liked_reviews", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]