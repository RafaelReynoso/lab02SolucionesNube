from django.db import models

class Contacto(models.Model):    
    nombre = models.CharField(max_length=50)    
    apellido = models.CharField(max_length=50)    
    email = models.EmailField(blank=True)    
    telefono = models.CharField(max_length=20, blank=True)    
