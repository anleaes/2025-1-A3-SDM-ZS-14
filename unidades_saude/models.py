from django.db import models

# Create your models here.

class UnidadeSaude(models.Model):
    nome = models.CharField(max_length= 100)
    endereco = models.CharField(max_length= 100)
    telefone = models.CharField(max_length= 100)

    def __str__(self):
        return f'{self.nome} - {self.endereco}'
    