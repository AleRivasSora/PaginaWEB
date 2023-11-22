
from django.urls import path
from portafolio import views

urlpatterns = [
    # Otras URLs
    path('proyecto/<int:proyecto_id>/', views.detalle_proyecto, name='detalle_proyecto'),
]
