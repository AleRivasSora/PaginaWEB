from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField
from django.db.models.fields import URLField
from django import forms
from django.utils import timezone


class Projecto(models.Model):
    titulo = CharField(max_length=100)
    descripcion = CharField(max_length=200)
    imagen = ImageField(upload_to='portafolio/images')
    url = URLField(blank=True)


    def __str__(self):
        return self.titulo


class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    asunto = models.CharField(max_length=50)
    mensaje = models.TextField(max_length=1000)
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.fecha_envio = timezone.now().strftime('%Y-%m-%d %H:%M')
        super(Contacto, self).save(*args, **kwargs)

    def __str__(self):
        hora = self.fecha_envio = timezone.now().strftime('%Y-%m-%d %H:%M')
        return self.asunto+ '                                          ' + str(hora)
