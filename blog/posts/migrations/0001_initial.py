# Generated by Django 5.1.2 on 2024-10-28 10:10

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("post_title", models.CharField(max_length=60)),
                ("post_content", models.TextField()),
                ("published_date", models.DateField(auto_now=True)),
                ("post_pages", models.IntegerField()),
                ("post_authors", models.IntegerField()),
            ],
        ),
    ]
