# Generated by Django 5.1.2 on 2024-10-28 10:14

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="post_pages",
        ),
    ]