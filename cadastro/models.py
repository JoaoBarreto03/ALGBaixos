from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    senha = models.CharField(max_length=20)
    confirmaSenha = models.CharField(max_length=20)
    def __str__ (self) -> str:
        return self.email

