from django.shortcuts import render, get_object_or_404 , redirect
from .models import Projecto
from django.http import HttpResponse
from .forms import ContactoForm
from django.contrib import messages
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

def proyectos(request):
    proyectos = Projecto.objects.all()

    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            
            form.save()
            form = ContactoForm()# cambia 'success_page' a la URL de tu página de éxito
        else:
            print(form.errors)
    else:
        form = ContactoForm()
        
    return render(request, 'ejemplo.html', {'proyectos': proyectos,'form': form, 'enviado':True})

def index(request):
    return render(request,'index.html')

def detalle_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Projecto, id=proyecto_id)
    return render(request, 'detalle_proyecto.html', {'proyecto': proyecto})