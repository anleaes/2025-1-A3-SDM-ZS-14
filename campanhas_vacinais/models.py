from django.db import models

# Create your models here.

class CampanhaVacinal(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=200)
    data_inicio = models.DateField()
    data_fim = models.DateField()