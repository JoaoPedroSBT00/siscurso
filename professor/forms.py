from django import forms
from .models import Professor

class ProfessorForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    password_confirm = forms.CharField(widget=forms.PasswordInput, required=True)
    
    class Meta:
        model = Professor
        fields = ['username', 'first_name', 'curriculo', 'formacao', 'password']
    labels = {
        'username': 'Usuário',
        'first_name': 'Nome',
        'password': 'Senha',
        }
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("As senhas não coincidem")
        
        return cleaned_data

class ProfessorUpdateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=False)
    
    class Meta:
        model = Professor
        fields = ['username', 'first_name', 'last_name', 'curriculo', 'formacao']