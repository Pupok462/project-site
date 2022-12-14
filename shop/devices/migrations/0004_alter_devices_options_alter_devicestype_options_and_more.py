# Generated by Django 4.1 on 2022-08-15 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("devices", "0003_devices_img"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="devices",
            options={"verbose_name_plural": "Devices"},
        ),
        migrations.AlterModelOptions(
            name="devicestype",
            options={"verbose_name_plural": "Devices Type"},
        ),
        migrations.AlterField(
            model_name="devices",
            name="img",
            field=models.ImageField(
                blank=True, null=True, upload_to="devices/static/img"
            ),
        ),
    ]
