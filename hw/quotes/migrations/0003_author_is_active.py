# Generated by Django 4.2 on 2024-03-17 11:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("quotes", "0002_alter_tag_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="author",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
    ]
