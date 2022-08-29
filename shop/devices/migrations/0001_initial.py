# Generated by Django 4.1 on 2022-08-11 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Laptop",
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
                ("company", models.CharField(max_length=64)),
                ("model", models.CharField(max_length=64)),
                ("price", models.FloatField(null=True)),
                ("description", models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="Phone",
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
                ("company", models.CharField(max_length=64)),
                ("model", models.CharField(max_length=64)),
                ("price", models.FloatField(null=True)),
                ("description", models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="Tablet",
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
                ("company", models.CharField(max_length=64)),
                ("model", models.CharField(max_length=64)),
                ("price", models.FloatField(null=True)),
                ("description", models.TextField(blank=True)),
            ],
        ),
    ]