from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        emailLog = request.POST.get('email')
        senhaLog = request.POST.get('senha')

        print(email)
        return HttpResponse('teste')


