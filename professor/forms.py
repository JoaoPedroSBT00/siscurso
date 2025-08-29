from django import forms
from django.contrib.auth.models import User
from .models import Professor

class ProfessorForm(forms.ModelForm):
    username = forms.CharField(max_length=150, label="Usuário")
    first_name = forms.CharField(max_length=150, label="Nome")
    last_name = forms.CharField(max_length=150, label="Sobrenome")
    password = forms.CharField(widget=forms.PasswordInput, label="Senha")
    curriculo = forms.CharField(widget=forms.Textarea, label="Currículo")
    formacao = forms.CharField(max_length=255, label="Formação")

    class Meta:
        model = Professor
        fields = ['username', 'first_name', 'last_name', 'password', 'curriculo', 'formacao']

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Esse nome de usuário já está em uso.")
        return username

class ProfessorUpdateForm(forms.ModelForm):
    username = forms.CharField(
        max_length=150,
        label="Usuário",
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )
    first_name = forms.CharField(max_length=150, label="Nome")
    last_name = forms.CharField(max_length=150, label="Sobrenome")
    password = forms.CharField(
        widget=forms.PasswordInput,
        required=False,
        label="Nova Senha (deixe em branco para manter a atual)"
    )
    curriculo = forms.CharField(widget=forms.Textarea, label="Currículo")
    formacao = forms.CharField(max_length=255, label="Formação")

    class Meta:
        model = Professor
        fields = ['username', 'first_name', 'last_name', 'curriculo', 'formacao', 'password']

    def __init__(self, *args, **kwargs):
        self.user_instance = kwargs.pop('user_instance', None)
        super().__init__(*args, **kwargs)

    def clean_username(self):
        username = self.cleaned_data['username']
        user_qs = User.objects.filter(username=username)
        if self.user_instance:
            user_qs = user_qs.exclude(pk=self.user_instance.pk)
        if user_qs.exists():
            raise forms.ValidationError("Esse nome de usuário já está em uso.")
        return username
