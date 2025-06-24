from django.db import models

class Agendamento(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('confirmado', 'Confirmado'),
        ('cancelado', 'Cancelado'),
        ('realizado', 'Realizado'),
    ]

    data_hora = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')

    usuario = models.ForeignKey(
        'usuarios.Usuario',
        on_delete=models.CASCADE,
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
        return f'{self.usuario.nome} - {self.vacina.nome} em {self.data_hora.strftime("%d/%m/%Y %H:%M")}'