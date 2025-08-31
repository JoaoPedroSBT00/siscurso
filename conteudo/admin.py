from django.contrib import admin
from .models import Conteudo

@admin.register(Conteudo)
class ConteudoAdmin(admin.ModelAdmin):
    list_display = ('curso', 'ordem', 'titulo')
    list_filter = ('curso',)
    search_fields = ('titulo', 'desc')
    ordering = ('curso', 'ordem')
