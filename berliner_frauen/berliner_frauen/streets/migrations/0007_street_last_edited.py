# Generated by Django 3.2.19 on 2023-06-28 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("streets", "0006_street_tags"),
    ]

    operations = [
        migrations.AddField(
            model_name="street",
            name="last_edited",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
