# Generated by Django 3.2.15 on 2023-06-15 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("streets", "0004_remove_district_district_image_path"),
    ]

    operations = [
        migrations.AddField(
            model_name="district",
            name="image_path",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
