from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        email = request.POST.get('emailLog')
        senha = request.POST.get('senhaLog')

        user = User.objects.get(email=email).first()

        if user:
            return HttpResponse('Já existe um usuário com esse username') 
       
        pessoa = Pessoa.objects.create_user(email=email, )

        pessoa = Pessoa(
            email = email,
            senha = senha
        )

from django.contrib.auth.models import User

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmaSenha = request.POST.get('confirma-senha')
        
        pessoa = Pessoa.objects.filter(email=email).first()

        if pessoa:
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

        username = sobrenome

        usuario = User.objects.create_user(username=username)
        pessoa.save()

        if senha == confirmaSenha:
            return HttpResponse('Usuário cadastrado com sucesso')
        else:
            return HttpResponse('erro')
        
