# Generated by Django 4.2.7 on 2023-11-29 01:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("students", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Student",
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
                ("firstname", models.CharField(max_length=255)),
                ("lastname", models.CharField(max_length=255)),
                ("phone", models.IntegerField(null=True)),
                ("joined_date", models.DateField(null=True)),
            ],
        ),
        migrations.DeleteModel(
            name="Member",
        ),
    ]
