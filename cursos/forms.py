from django import forms
from .models import Curso
from professor.models import Professor

class CursoForm(forms.ModelForm):
    nome = forms.CharField(max_length=255, label="Nome")
    ch = forms.IntegerField(label="Carga Horária")
    descricao = forms.CharField(widget=forms.Textarea, label="Descrição")
    professor = forms.ModelChoiceField(
        queryset=Professor.objects.all(),
        empty_label="Selecione um professor",
        label="Professor"
    )

    class Meta:
        model = Curso
        fields = ['nome', 'ch', 'descricao', 'professor']