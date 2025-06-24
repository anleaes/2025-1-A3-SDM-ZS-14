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