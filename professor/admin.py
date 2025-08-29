from django.contrib import admin
from .models import Professor

@admin.register(Professor)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ['user', 'formacao', 'curriculo']
