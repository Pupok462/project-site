# Generated by Django 4.1 on 2022-08-18 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("devices", "0008_alter_devices_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="Slider",
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
                ("image", models.ImageField(upload_to="images/slider")),
                ("title", models.CharField(max_length=150)),
                ("sub_title", models.CharField(max_length=100)),
            ],
        ),
    ]
