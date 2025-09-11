from django import forms
from .models import Conteudo
from cursos.models import Curso

class ConteudoForm(forms.ModelForm):
    ordem = forms.IntegerField(label="Ordem", min_value=1)
    titulo = forms.CharField(max_length=255, label="Título")
    desc = forms.CharField(widget=forms.Textarea, label="Descrição")
    m_apoio = forms.FileField(label="Material de Apoio", required=False)
    curso = forms.ModelChoiceField(
        queryset=Curso.objects.all(),
        empty_label="Selecione um curso",
        label="Curso"
    )

    class Meta:
        model = Conteudo
        fields = ['ordem', 'titulo', 'desc', 'm_apoio', 'curso']