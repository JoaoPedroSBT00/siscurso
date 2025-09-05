from django import forms
from .models import Aluno

class AlunoForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput, 
        required=True,
        label="Senha"
    )
    password_confirm = forms.CharField(
        widget=forms.PasswordInput, 
        required=True,
        label="Confirmar Senha"
    )
    
    class Meta:
        model = Aluno
        fields = ['username', 'first_name', 'last_name', 'data_nascimento']
        labels = {
            'username': 'Usuário',
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'data_nascimento': 'Data de Nascimento'
        }
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("As senhas não coincidem")
        
        return cleaned_data
    
    def save(self, commit=True):
        aluno = super().save(commit=False)
        password = self.cleaned_data.get('password')
        if password:
            aluno.set_password(password)
        if commit:
            aluno.save()
        return aluno

class AlunoUpdateForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput, 
        required=False,
        label="Nova Senha (deixe em branco para manter a atual)"
    )
    
    class Meta:
        model = Aluno
        fields = ['username', 'first_name', 'last_name', 'data_nascimento']
        labels = {
            'username': 'Usuário',
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'data_nascimento': 'Data de Nascimento'
        }
        widgets = {
            'username': forms.TextInput(attrs={'readonly': 'readonly'})
        }
    
    def save(self, commit=True):
        aluno = super().save(commit=False)
        password = self.cleaned_data.get('password')
        if password:
            aluno.set_password(password)
        if commit:
            aluno.save()
        return aluno
    
    