# Generated by Django 3.2.19 on 2023-06-28 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_alter_blogpost_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogpost",
            name="published",
            field=models.DateField(auto_now=True),
        ),
    ]
