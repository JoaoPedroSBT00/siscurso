from django.contrib import admin
from django.urls import path
from .views import registrar
from django.contrib.auth import views as auth_views
from professor import views as views_professor
from aluno import views as views_aluno
from cursos import views as views_curso
from conteudo import views as views_conteudo
from aluno_curso import views as views_matricula
from . import views

urlpatterns = [   
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path("registrar/", registrar, name="registrar"),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
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
    #curso
    path('curso/', views_curso.index, name="index-curso"),
    path('curso/adicionar/', views_curso.add, name="add-curso"),
    path('curso/editar/<int:pk>/', views_curso.edit, name="edit-curso"),
    path('curso/remover/<int:pk>/', views_curso.remove, name="remove-curso"),
    path('curso/<int:pk>/', views_curso.detalhe, name="detail-curso"),
    #conteudo
    path('conteudo/', views_conteudo.index, name="index-conteudo"),
    path('conteudo/adicionar/', views_conteudo.add, name="add-conteudo"),
    path('conteudo/editar/<int:pk>/', views_conteudo.edit, name="edit-conteudo"),
    path('conteudo/remover/<int:pk>/', views_conteudo.remove, name="remove-conteudo"),
    path('conteudo/<int:pk>/', views_conteudo.detalhe, name="detail-conteudo"),
    #matricula
    path('matricula/', views_matricula.index, name="index-matricula"),
    path('matricula/adicionar/', views_matricula.add, name="add-matricula"),
    path('matricula/editar/<int:pk>/', views_matricula.edit, name="edit-matricula"),
    path('matricula/remover/<int:pk>/', views_matricula.remove, name="remove-matricula"),
    path('matricula/<int:pk>/', views_matricula.detalhe, name="detail-matricula"),
]
