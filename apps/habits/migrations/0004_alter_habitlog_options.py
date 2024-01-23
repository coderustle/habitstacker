# Generated by Django 5.0 on 2024-01-23 14:07

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("habits", "0003_alter_habitlog_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="habitlog",
            options={
                "default_permissions": ("add", "change", "delete"),
                "permissions": (("view_habit_log", "View Habit Log Objects"),),
            },
        ),
    ]
