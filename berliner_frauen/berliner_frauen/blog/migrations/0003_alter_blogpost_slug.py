# Generated by Django 3.2.19 on 2023-06-28 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpost_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='slug',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]