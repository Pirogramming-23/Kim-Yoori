# Generated by Django 5.2.4 on 2025-07-11 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Review",
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
                ("title", models.CharField(max_length=100)),
                ("release_year", models.IntegerField()),
                ("director", models.CharField(max_length=100)),
                ("actors", models.CharField(max_length=200)),
                ("genre", models.CharField(max_length=50)),
                ("rating", models.IntegerField()),
                ("running_time", models.IntegerField(help_text="단위: 분")),
                ("content", models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name="Reveiw",
        ),
    ]
