# Generated by Django 4.2 on 2023-04-28 02:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portafolio", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contacto",
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
                ("nombre", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254)),
                ("telefono", models.CharField(max_length=20)),
                ("asunto", models.CharField(max_length=50)),
                ("mensaje", models.TextField(max_length=1000)),
            ],
        ),
    ]