# Generated by Django 4.2 on 2023-10-22 21:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portafolio", "0006_alter_projecto_explicacion"),
    ]

    operations = [
        migrations.AlterField(
            model_name="projecto",
            name="explicacion",
            field=models.TextField(default=""),
        ),
    ]
