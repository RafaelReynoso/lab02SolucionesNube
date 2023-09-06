from django.shortcuts import render, get_object_or_404, redirect
from .models import Contacto
from .forms import ContactoForm


def lista_contactos(request):    
    contactos = Contacto.objects.all()    
    return render(request, 'agenda/lista_contactos.html', {'contactos': contactos})
