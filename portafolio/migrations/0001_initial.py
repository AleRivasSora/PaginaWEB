# Generated by Django 4.2 on 2023-04-25 20:16

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Projecto",
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
                ("titulo", models.CharField(max_length=100)),
                ("descripcion", models.CharField(max_length=200)),
                ("imagen", models.ImageField(upload_to="portafolio/images")),
                ("url", models.URLField(blank=True)),
            ],
        ),
    ]
