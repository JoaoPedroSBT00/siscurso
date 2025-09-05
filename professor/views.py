from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import Professor
from .forms import ProfessorForm, ProfessorUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.contrib import messages

@login_required
@permission_required('professor.view_professor', raise_exception=True)
def index(request):
    professores = Professor.objects.all()
    return render(request, "professor/index.html", {"professores": professores})

@login_required
@permission_required('professor.add_professor', raise_exception=True)
def add(request):

    if not request.user.has_perm('professor.add_professor'):
        messages.error(request, "Você não tem permissão para adicionar alunos.")
        return redirect('index-professor') 

    if request.method == "POST":
        form = ProfessorForm(request.POST)
        if form.is_valid():
            professor = form.save(commit=False)
            
            password = form.cleaned_data.get('password')
            if password:
                professor.set_password(password)

            professor.save()

            professor_group, created = Group.objects.get_or_create(name="professores")
            professor.groups.add(professor_group)  # <<-- aqui é groups, não group

            
            return redirect("index-professor")
    else:
        form = ProfessorForm()
    return render(request, "professor/add.html", {"form": form})

@login_required
@permission_required('professor.change_professor', raise_exception=True)
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
@permission_required('professor.delete_professor', raise_exception=True)
def remove(request, pk):
    professor = get_object_or_404(Professor, pk=pk)
    professor.delete() 
    return redirect("index-professor")

@login_required
@permission_required('professor.view_professor', raise_exception=True)
def detalhe(request, pk):
    professor = get_object_or_404(Professor, pk=pk)
    return render(request, "professor/detalhe.html", {"professor": professor})