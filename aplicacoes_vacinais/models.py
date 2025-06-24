from django.db import models

# Create your models here.

class AplicacaoVacina(models.Model):
    data_aplicacao = models.DateField()
    dose = models.PositiveIntegerField()

    medico = models.ForeignKey(
        'medicos.Medico',
        on_delete=models.CASCADE,
        related_name='aplicacoes_realizadas' 

    )

    usuario = models.ForeignKey(
        'usuarios.Usuario',
        on_delete=models.CASCADE,
        related_name='aplicacoes_recebidas'
    )