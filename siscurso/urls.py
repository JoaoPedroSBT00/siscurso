from django.contrib import admin
from django.urls import path
from professor import views as views_professor
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #professor
    path('professor/', views_professor.index, name="index-professor"),
    path('professor/adicionar/', views_professor.add, name="add-professor"),
    path('professor/editar/<int:id_professor>/', views_professor.edit, name="edit-professor"),
    path('professor/remover/<int:id_professor>/', views_professor.remove, name="remove-professor"),
    path('professor/<int:id_professor>/', views_professor.detalhe, name="detail-professor"),
    path('', views.home, name='home')
    #aluno
    
]
