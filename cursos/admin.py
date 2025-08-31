from django.contrib import admin
from .models import Curso

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ch', 'professor')
    list_filter = ('professor',)
    search_fields = ('nome', 'descricao')
