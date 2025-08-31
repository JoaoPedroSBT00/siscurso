from django.shortcuts import render, redirect, get_object_or_404
from .models import Conteudo
from .forms import ConteudoForm

# Listar conteudos
def index(request):
    conteudos = Conteudo.objects.all()
    return render(request, "conteudo/index.html", {"conteudos": conteudos})

# Adicionar conteudo
def add(request):
    if request.method == "POST":
        form = ConteudoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index-conteudo")
    else:
        form = ConteudoForm()
    return render(request, "conteudo/add.html", {"form": form})

# Editar conteudo
def edit(request, pk):
    conteudo = get_object_or_404(Conteudo, pk=pk)
    
    if request.method == "POST":
        form = ConteudoForm(request.POST, instance=conteudo)
        if form.is_valid():
            form.save()
            return redirect("index-conteudo")
    else:
        form = ConteudoForm(instance=conteudo)

    return render(request, "conteudo/edit.html", {"form": form})

# Remover conteudo
def remove(request, pk):
    conteudo = get_object_or_404(Conteudo, pk=pk)
    conteudo.delete()
    return redirect("index-conteudo")

def detalhe(request, pk):
    conteudo = get_object_or_404(Conteudo, pk=pk)
    return render(request, "conteudo/detalhe.html", {"conteudo": conteudo})
