from django import forms
from django.contrib.auth.models import User
from .models import Aluno

class AlunoForm(forms.ModelForm):
    username = forms.CharField(max_length=150, label="Usuário")
    first_name = forms.CharField(max_length=150, label="Nome")
    last_name = forms.CharField(max_length=150, label="Sobrenome")
    password = forms.CharField(widget=forms.PasswordInput, label="Senha")

    class Meta:
        model = Aluno
        fields = ['username', 'first_name', 'last_name', 'password', 'data_nascimento']

class AlunoUpdateForm(forms.ModelForm):
    username = forms.CharField(
        max_length=150, 
        label="Usuário",
        widget=forms.TextInput(attrs={'readonly': 'readonly'})  # Mude de disabled para readonly
    )
    first_name = forms.CharField(max_length=150, label="Nome")
    last_name = forms.CharField(max_length=150, label="Sobrenome")
    password = forms.CharField(
        widget=forms.PasswordInput, 
        required=False, 
        label="Nova Senha (deixe em branco para manter a atual)"
    )

    class Meta:
        model = Aluno
        fields = ['username', 'first_name', 'last_name', 'data_nascimento', 'password']