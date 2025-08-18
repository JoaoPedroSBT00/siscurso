from django.shortcuts import render

def home(request):
    return render(request, 'others/home.html')