from django.shortcuts import render, redirect, get_object_or_404
from .models import AlunoCurso
from .forms import AlunoCursoForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required

@login_required
@permission_required('aluno_curso.view_alunocurso', raise_exception=True)
def index(request):
    matriculas = AlunoCurso.objects.all()
    return render(request, "aluno_curso/index.html", {"matriculas": matriculas})

@login_required
@permission_required('aluno_curso.add_alunocurso', raise_exception=True)
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
@permission_required('aluno_curso.change_alunocurso', raise_exception=True)
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
@permission_required('aluno_curso.delete_alunocurso', raise_exception=True)
def remove(request, pk):
    matricula = get_object_or_404(AlunoCurso, pk=pk)
    matricula.delete()
    return redirect("index-matricula")

@login_required
@permission_required('aluno_curso.view_alunocurso', raise_exception=True)
def detalhe(request, pk):
    matricula = get_object_or_404(AlunoCurso, pk=pk)
    return render(request, "aluno_curso/detalhe.html", {"matricula": matricula})
