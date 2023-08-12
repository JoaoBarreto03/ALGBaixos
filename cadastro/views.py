from django.shortcuts import render
from django.http import HttpResponse
from .models import Pessoa

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmaSenha = request.POST.get('confirma-senha')
        
        pessoa = Pessoa.objects.filter(email=email)

        if pessoa.exists():
            return HttpResponse('Esse usuário já existe!')
        
        pessoa = Pessoa(
            nome = nome,
            sobrenome = sobrenome,
            email = email,
            senha = senha,
            confirmaSenha = confirmaSenha
        )

        print(nome)
        print(email)

        pessoa.save()

        if senha == confirmaSenha:
            return HttpResponse('teste')
        else:
            return HttpResponse('erro')