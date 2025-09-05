from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Professor
from .forms import ProfessorForm, ProfessorUpdateForm
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    professores = Professor.objects.all()
    return render(request, "professor/index.html", {"professores": professores})

@login_required
def add(request):
    if request.method == "POST":
        form = ProfessorForm(request.POST)
        if form.is_valid():
            professor = form.save(commit=False)
            
            password = form.cleaned_data.get('password')
            if password:
                professor.set_password(password)
            
            professor.save()
            return redirect("index-professor")
    else:
        form = ProfessorForm()
    return render(request, "professor/add.html", {"form": form})

@login_required
def edit(request, pk):
    professor = get_object_or_404(Professor, pk=pk)

    if request.method == "POST":
        form = ProfessorUpdateForm(request.POST, instance=professor)
        if form.is_valid():
            password = form.cleaned_data.get('password')
            if password:
                professor.set_password(password)
            form.save()
            return redirect("index-professor")
    else:
        form = ProfessorUpdateForm(instance=professor)
    
    return render(request, "professor/edit.html", {"form": form})

@login_required
def remove(request, pk):
    professor = get_object_or_404(Professor, pk=pk)
    professor.delete() 
    return redirect("index-professor")

def detalhe(request, pk):
    professor = get_object_or_404(Professor, pk=pk)
    return render(request, "professor/detalhe.html", {"professor": professor})