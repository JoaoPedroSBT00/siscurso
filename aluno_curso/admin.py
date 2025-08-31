from django.contrib import admin
from .models import AlunoCurso

@admin.register(AlunoCurso)
class AlunoCursoAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'curso', 'dt_mat', 'status')
    list_filter = ('status', 'curso', 'dt_mat')
    search_fields = ('aluno__user__first_name', 'aluno__user__last_name', 'curso__nome')
    date_hierarchy = 'dt_mat'
