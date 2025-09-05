from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Aluno
from django.contrib.auth.models import Group
from .forms import AlunoForm, AlunoUpdateForm
from django.contrib import messages


@login_required
@permission_required('aluno.view_aluno', raise_exception=True)
def index(request):
    alunos = Aluno.objects.all()
    return render(request, 'aluno/index.html', {'alunos': alunos})

@login_required
@permission_required('aluno.add_aluno', raise_exception=True)
def add(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            aluno = form.save(commit=False) 

            aluno.save()

            aluno_group, created = Group.objects.get_or_create(name="alunos")
            aluno.groups.add(aluno_group)  # <<-- aqui é groups, não group

            return redirect('index-aluno')
    else:
        form = AlunoForm()
    return render(request, 'aluno/add.html', {'form': form})

@login_required
@permission_required('aluno.change_aluno', raise_exception=True)
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
@permission_required('aluno.delete_aluno', raise_exception=True)
def remove(request, id_aluno):
    aluno = get_object_or_404(Aluno, id=id_aluno)
    aluno.delete() 
    return redirect('index-aluno')

@login_required
@permission_required('aluno.view_aluno', raise_exception=True)
def detalhe(request, id_aluno):
    aluno = get_object_or_404(Aluno, id=id_aluno)
    return render(request, 'aluno/detail.html', {'aluno': aluno})