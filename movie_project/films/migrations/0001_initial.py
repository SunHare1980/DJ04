# Generated by Django 5.1 on 2024-08-31 14:26

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="films",
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
                (
                    "title",
                    models.CharField(max_length=50, verbose_name="Название фильма"),
                ),
                (
                    "short_description",
                    models.CharField(
                        max_length=200, verbose_name="Краткое описание фильма"
                    ),
                ),
                ("text", models.TextField(verbose_name="Отзыв")),
            ],
            options={
                "verbose_name": "Фильм",
                "verbose_name_plural": "Фильмы",
            },
        ),
    ]
