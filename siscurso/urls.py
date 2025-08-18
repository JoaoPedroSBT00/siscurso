"""
URL configuration for siscurso project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from professor import views as views_professor

urlpatterns = [
    path('admin/', admin.site.urls),
    #professor
    path('professor/', views_professor.index, name="index-professor"),
    path('professor/adicionar/', views_professor.add, name="add-professor"),
    path('professor/editar/<int:id_professor>/', views_professor.edit, name="edit-professor"),
    path('professor/remover/<int:id_professor>/', views_professor.remove, name="remove-professor"),
    path('professor/<int:id_professor>/', views_professor.detalhe, name="detail-professor"),
]
