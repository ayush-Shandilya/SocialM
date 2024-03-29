# Generated by Django 4.1.1 on 2022-11-04 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("profile_pic", models.ImageField(upload_to="profile_pic/")),
                ("bio", models.TextField(blank=True, max_length=160, null=True)),
            ],
        ),
    ]
