# Generated by Django 5.1.2 on 2024-10-30 06:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0008_alter_post_post_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="post_content",
            field=models.TextField(max_length=150),
        ),
    ]
