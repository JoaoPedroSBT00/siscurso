from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Aluno
from .forms import AlunoForm, AlunoUpdateForm

@login_required
def index(request):
    alunos = Aluno.objects.all()
    return render(request, 'aluno/index.html', {'alunos': alunos})

@login_required
def add(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('index-aluno')
    else:
        form = AlunoForm()
    return render(request, 'aluno/add.html', {'form': form})

@login_required
def edit(request, id_aluno):
    aluno = get_object_or_404(Aluno, id=id_aluno)
    if request.method == 'POST':
        form = AlunoUpdateForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save() 
            return redirect('index-aluno')
    else:
        form = AlunoUpdateForm(instance=aluno)
    return render(request, 'aluno/edit.html', {'form': form, 'aluno': aluno})

@login_required
def remove(request, id_aluno):
    aluno = get_object_or_404(Aluno, id=id_aluno)
    aluno.delete() 
    return redirect('index-aluno')

@login_required
def detalhe(request, id_aluno):
    aluno = get_object_or_404(Aluno, id=id_aluno)
    return render(request, 'aluno/detail.html', {'aluno': aluno})