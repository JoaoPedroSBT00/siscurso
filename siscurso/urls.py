from django.contrib import admin
from django.urls import path
from professor import views as views_professor
from aluno import views as views_aluno
from . import views

urlpatterns = [   
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    #professor
    path('professor/', views_professor.index, name="index-professor"),
    path('professor/adicionar/', views_professor.add, name="add-professor"),
    path('professor/editar/<int:pk>/', views_professor.edit, name="edit-professor"),
    path('professor/remover/<int:pk>/', views_professor.remove, name="remove-professor"),
    path('professor/<int:pk>/', views_professor.detalhe, name="detail-professor"),
    #aluno
    path('aluno/', views_aluno.index, name="index-aluno"),
    path('aluno/adicionar/', views_aluno.add, name="add-aluno"),
    path('aluno/editar/<int:id_aluno>/', views_aluno.edit, name="edit-aluno"),
    path('aluno/remover/<int:id_aluno>/', views_aluno.remove, name="remove-aluno"),
    path('aluno/<int:id_aluno>/', views_aluno.detalhe, name="detail-aluno"),
]
