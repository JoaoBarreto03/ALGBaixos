from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    senha = models.CharField(max_length=20)
    confirmaSenha = models.CharField(max_length=20)
    def __str__ (self) -> str:
        return self.email

class Login(models.Model):
    emailLog = models.EmailField(max_length=100)
    senhaLog = models.CharField(max_length=20)

    def __str__ (self) -> str:
        return self.emailLog
