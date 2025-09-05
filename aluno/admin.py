from django.contrib import admin
from .models import Aluno

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ['username', 'get_full_name', 'matricula', 'data_nascimento']
    list_filter = ['data_nascimento']
    search_fields = ['username', 'first_name', 'last_name', 'matricula']
    
    def get_full_name(self, obj):
        return obj.get_full_name()
    get_full_name.short_description = 'Nome completo'