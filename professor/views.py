from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Professor
from .forms import ProfessorForm



def index(request):

    professores = Professor.objects.all()

    return render(request, 'professor/index.html', {'professores': professores})


def add(request):

    if request.method == 'POST':
       form = ProfessorForm(request.POST)

       if form.is_valid():
            form.save()
            return HttpResponseRedirect('/professor/')
    else:
        form = ProfessorForm()

    return render(request, 'professor/adicionar.html', { 'form': form})



def edit(request, id_professor):

    professores = Professor.objects.get(id=id_professor)

    if request.method == 'POST':
       form = ProfessorForm(request.POST, instance=professores)

       if form.is_valid():
            form.save()
            return HttpResponseRedirect('/professor/')
    else:
        form = ProfessorForm()

    return render(request, 'professor/editar.html', {'form': form})

def remove(request, id_pessoa):

    professores = Professor.objects.filter(id=id_pessoa)
    professores.delete()

    return HttpResponseRedirect('/professor/')


def detalhe(request, id_pessoa):
    professores = Professor.objects.get(id=id_pessoa)

    return render(request, 'professor/detalhe.html', {'professores': professores})
