from django.db import models

from unidades_saude.models import UnidadeSaude
from vacinas.models import Vacina

# Create your models here.

class EstoqueVacina(models.Model):
    quantidade_disponsivel = models.DecimalField(max_digits=10, decimal_places=2)
    vacina = models.ForeignKey(Vacina, on_delete=models.CASCADE)
    unidade = models.ForeignKey(UnidadeSaude, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.vacina.nome} - {self.unidade.nome}'