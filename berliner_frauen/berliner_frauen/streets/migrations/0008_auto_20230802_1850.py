# Generated by Django 3.2.20 on 2023-08-02 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("streets", "0007_street_last_edited"),
    ]

    operations = [
        migrations.AddField(
            model_name="street",
            name="latitude",
            field=models.FloatField(default=1.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="street",
            name="longitude",
            field=models.FloatField(default=1.0),
            preserve_default=False,
        ),
    ]
