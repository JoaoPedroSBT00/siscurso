from django.shortcuts import render, redirect, get_object_or_404
from .models import Aluno
from .forms import AlunoForm
from .forms import AlunoUpdateForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Aluno
from .forms import AlunoForm


@login_required
def index(request):
    alunos = Aluno.objects.all()
    return render(request, 'aluno/index.html', {'alunos': alunos})

@login_required
def add(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            # Criar usuário
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name']
            )
            # Criar aluno
            aluno = form.save(commit=False)
            aluno.user = user
            aluno.save()
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
            aluno = form.save(commit=False)
            user = aluno.user
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()
            aluno.save()
            return redirect('index-aluno')
    else:
        form = AlunoUpdateForm(instance=aluno, initial={
            'username': aluno.user.username,
            'first_name': aluno.user.first_name,
            'last_name': aluno.user.last_name,
        })
    return render(request, 'aluno/edit.html', {'form': form, 'aluno': aluno})

@login_required
def remove(request, id_aluno):
    aluno = get_object_or_404(Aluno, id=id_aluno)
    if request.method == 'POST':
        aluno.user.delete()  # remove também o usuário ligado
        aluno.delete()
        return redirect('index-aluno')
    return render(request, 'aluno/remove.html', {'aluno': aluno})


@login_required
def detalhe(request, id_aluno):
    aluno = get_object_or_404(Aluno, id=id_aluno)
    return render(request, 'aluno/detail.html', {'aluno': aluno})
