# Generated by Django 5.1.2 on 2024-10-30 06:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0004_alter_post_post_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="post_description",
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="post",
            name="post_image",
            field=models.ImageField(default="", upload_to="images/"),
        ),
    ]
