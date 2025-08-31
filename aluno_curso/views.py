from django.shortcuts import render, redirect, get_object_or_404
from .models import AlunoCurso
from .forms import AlunoCursoForm
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    matriculas = AlunoCurso.objects.all()
    return render(request, "aluno_curso/index.html", {"matriculas": matriculas})

@login_required
def add(request):
    if request.method == "POST":
        form = AlunoCursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index-matricula")
    else:
        form = AlunoCursoForm()
    return render(request, "aluno_curso/add.html", {"form": form})

@login_required
def edit(request, pk):
    matricula = get_object_or_404(AlunoCurso, pk=pk)
    
    if request.method == "POST":
        form = AlunoCursoForm(request.POST, instance=matricula)
        if form.is_valid():
            form.save()
            return redirect("index-matricula")
    else:
        form = AlunoCursoForm(instance=matricula)

    return render(request, "aluno_curso/edit.html", {"form": form})

@login_required
def remove(request, pk):
    matricula = get_object_or_404(AlunoCurso, pk=pk)
    matricula.delete()
    return redirect("index-matricula")

def detalhe(request, pk):
    matricula = get_object_or_404(AlunoCurso, pk=pk)
    return render(request, "aluno_curso/detalhe.html", {"matricula": matricula})
