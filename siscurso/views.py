from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django


def home(request):
    return render(request, 'others/home.html')

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        if User.objects.filter(username=username).exists():
            return HttpResponse('Usuario ja existe')
            return redirect("cadastro") 

        user = User.objects.create_user(username=username, password=senha)
        user.save()

        return render(request, 'login.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
        
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login_django(request, user)
            return render(request, 'others/home.html')
        else:
            return HttpResponse('email ou senha incorreto')
        
def logout_view(request):
    logout(request)
    return redirect('login')

