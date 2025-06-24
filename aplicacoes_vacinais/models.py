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

    vacina = models.ForeignKey(
        'vacinas.Vacina',
        on_delete=models.CASCADE,
    )

    unidade = models.ForeignKey(
        'unidades_saude.UnidadeSaude',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.usuario.nome} - {self.vacina.nome} - Dose {self.dose}'

