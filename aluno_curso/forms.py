from django import forms
from .models import AlunoCurso
from aluno.models import Aluno
from cursos.models import Curso

class AlunoCursoForm(forms.ModelForm):
    aluno = forms.ModelChoiceField(
        queryset=Aluno.objects.all(),
        empty_label="Selecione um aluno",
        label="Aluno"
    )
    curso = forms.ModelChoiceField(
        queryset=Curso.objects.all(),
        empty_label="Selecione um curso",
        label="Curso"
    )
    dt_mat = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="Data de Matrícula"
    )
    status = forms.ChoiceField(
        choices=AlunoCurso.STATUS_CHOICES,
        label="Status"
    )

    class Meta:
        model = AlunoCurso
        fields = ['aluno', 'curso', 'dt_mat', 'status']