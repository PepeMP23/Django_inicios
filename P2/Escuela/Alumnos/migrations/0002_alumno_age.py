# Generated by Django 4.2.5 on 2023-09-13 01:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Alumnos", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="alumno",
            name="age",
            field=models.IntegerField(null=True),
        ),
    ]
