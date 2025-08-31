from django.db import models
from professor.models import Professor

class Curso(models.Model):
    nome = models.CharField(max_length=255)
    ch = models.IntegerField(verbose_name="Carga Horária")
    descricao = models.TextField()
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
