from django.db import models

from campanhas_vacinais.models import CampanhaVacinal

# Create your models here.

class CampanhaVacinalVacina(models.Model):
    campanha = models.ForeignKey(CampanhaVacinal, on_delete=models.CASCADE)
    vacina = models.ForeignKey('vacinas.Vacina', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('campanha', 'vacina')

    def __str__(self):
        return f'{self.campanha.nome} - {self.vacina.nome}'