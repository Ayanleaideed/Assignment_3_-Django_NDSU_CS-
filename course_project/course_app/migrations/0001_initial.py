# Generated by Django 5.0.2 on 2024-02-28 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
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
                ("course_id", models.CharField(max_length=10)),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("credits", models.IntegerField()),
                ("instructor", models.CharField(max_length=100)),
                ("start_date", models.DateField()),
                ("prerequisites", models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]