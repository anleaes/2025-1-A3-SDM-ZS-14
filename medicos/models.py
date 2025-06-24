from django.db import models

from usuarios.models import Usuario

# Create your models here.

class Medico(Usuario):
    registro_profissional = models.CharField(max_length=50, unique=True)
    especialidade = models.CharField(max_length=100)
