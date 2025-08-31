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
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            curriculo = form.cleaned_data['curriculo']
            formacao = form.cleaned_data['formacao']

            user = User.objects.create_user(
                username=username,
                password=password,
                first_name=first_name,
                last_name=last_name
            )

            Professor.objects.create(
                user=user,
                curriculo=curriculo,
                formacao=formacao
            )

            return redirect("index-professor")
    else:
        form = ProfessorForm()
    return render(request, "professor/add.html", {"form": form})

@login_required
def edit(request, pk):
    professor = get_object_or_404(Professor, pk=pk)
    user = professor.user

    if request.method == "POST":
        form = ProfessorUpdateForm(request.POST, instance=professor, user_instance=user)
        if form.is_valid():
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            if form.cleaned_data['password']:
                user.set_password(form.cleaned_data['password'])
            user.save()

            professor.curriculo = form.cleaned_data['curriculo']
            professor.formacao = form.cleaned_data['formacao']
            professor.save()

            return redirect("index-professor")
    else:
        form = ProfessorUpdateForm(
            instance=professor,
            user_instance=user,
            initial={
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'curriculo': professor.curriculo,
                'formacao': professor.formacao
            }
        )

    return render(request, "professor/edit.html", {"form": form})

@login_required
def remove(request, pk):
    professor = get_object_or_404(Professor, pk=pk)
    user = professor.user
    professor.delete()
    user.delete()
    return redirect("index-professor")


def detalhe(request, pk):
    professor = get_object_or_404(Professor, pk=pk)
    return render(request, "professor/detalhe.html", {"professor": professor})
