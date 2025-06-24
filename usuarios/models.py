from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length= 100, null= False)
    cpf = models.CharField(max_length= 20, null = False, unique= True)
    data_nascimento = models.DateField(null = False)
    sexo = models.CharField(max_length=10, choices=[('M', 'Masculino'), ('F', 'Feminino')])
    email = models.EmailField(null = False)
    telefone = models.CharField(max_length= 20)
    
    def __str__(self):
        return f'{self.nome} - {self.cpf}'
    