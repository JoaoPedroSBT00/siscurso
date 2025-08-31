from django.shortcuts import render, redirect, get_object_or_404
from .models import Curso
from .forms import CursoForm

# Listar cursos
def index(request):
    cursos = Curso.objects.all()
    return render(request, "cursos/index.html", {"cursos": cursos})

# Adicionar curso
def add(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index-curso")
    else:
        form = CursoForm()
    return render(request, "cursos/add.html", {"form": form})

# Editar curso
def edit(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    
    if request.method == "POST":
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect("index-curso")
    else:
        form = CursoForm(instance=curso)

    return render(request, "cursos/edit.html", {"form": form})

# Remover curso
def remove(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    curso.delete()
    return redirect("index-curso")

def detalhe(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    return render(request, "cursos/detalhe.html", {"curso": curso})
