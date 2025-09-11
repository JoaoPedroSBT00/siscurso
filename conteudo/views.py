from django.shortcuts import render, redirect, get_object_or_404
from .models import Conteudo
from .forms import ConteudoForm
from django.contrib.auth.decorators import login_required, permission_required

@login_required
@permission_required('conteudo.view_conteudo', raise_exception=True)
def index(request):
    conteudos = Conteudo.objects.all()
    return render(request, "conteudo/index.html", {"conteudos": conteudos})

@login_required
@permission_required('conteudo.add_conteudo', raise_exception=True)
def add(request):
    if request.method == "POST":
        form = ConteudoForm(request.POST, request.FILES)
        if form.is_valid():
            conteudo = form.save(commit=False)
            if "m_apoio" in request.FILES:
                conteudo.m_apoio = request.FILES["m_apoio"].read()  # <- converte para bytes
            conteudo.save()
            return redirect("index-conteudo")
    else:
        form = ConteudoForm()
    return render(request, "conteudo/add.html", {"form": form})


@login_required
@permission_required('conteudo.change_conteudo', raise_exception=True)
def edit(request, pk):
    conteudo = get_object_or_404(Conteudo, pk=pk)

    if request.method == "POST":
        form = ConteudoForm(request.POST, request.FILES, instance=conteudo)
        if form.is_valid():
            conteudo = form.save(commit=False)
            if "m_apoio" in request.FILES:
                conteudo.m_apoio = request.FILES["m_apoio"].read()
            conteudo.save()
            return redirect("index-conteudo")
    else:
        form = ConteudoForm(instance=conteudo)

    return render(request, "conteudo/edit.html", {"form": form})

@login_required
@permission_required('conteudo.delete_conteudo', raise_exception=True)
def remove(request, pk):
    conteudo = get_object_or_404(Conteudo, pk=pk)
    conteudo.delete()
    return redirect("index-conteudo")

@login_required
@permission_required('conteudo.view_conteudo', raise_exception=True)
def detalhe(request, pk):
    conteudo = get_object_or_404(Conteudo, pk=pk)
    return render(request, "conteudo/detalhe.html", {"conteudo": conteudo})
