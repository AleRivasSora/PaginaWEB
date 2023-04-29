# Generated by Django 4.2 on 2023-04-29 16:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("portafolio", "0003_projecto_fecha_envio"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="projecto",
            name="fecha_envio",
        ),
        migrations.AddField(
            model_name="contacto",
            name="fecha_envio",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
