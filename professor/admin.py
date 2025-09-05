from django.contrib import admin
from .models import Professor

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    # Use campos diretamente do Professor (que herda de User)
    list_display = ['username', 'first_name', 'last_name', 'formacao']
    list_filter = ['formacao']
    search_fields = ['username', 'first_name', 'last_name', 'formacao']
    
    # Opcional: método para mostrar nome completo
    def nome_completo(self, obj):
        return obj.get_full_name()
    nome_completo.short_description = 'Nome completo'