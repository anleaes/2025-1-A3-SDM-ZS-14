from django.db import models

from campanhas_vacinais.models import CampanhaVacinal

# Create your models here.

class CampanhaVacinalVacina(models.Model):
    campanha = models.ForeignKey(CampanhaVacinal, on_delete=models.CASCADE)
    vacina = models.ForeignKey('vacinas.Vacina', on_delete=models.CASCADE)