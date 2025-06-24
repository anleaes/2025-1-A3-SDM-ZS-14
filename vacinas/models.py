from django.db import models

# Create your models here.

class Vacina(models.Model):
    nome = models.CharField(max_length= 100)
    descricao = models.CharField(max_length= 200)
    fabricante = models.CharField(max_length= 100)
    doses_recomendadas = models.IntegerField()
