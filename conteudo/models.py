from django.db import models
from cursos.models import Curso

class Conteudo(models.Model):
    ordem = models.PositiveIntegerField()
    titulo = models.CharField(max_length=255)
    desc = models.TextField(verbose_name="Descrição")
    m_apoio = models.BlobField(verbose_name="Material de Apoio")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    class Meta:
        ordering = ['curso', 'ordem']
        verbose_name = "Conteúdo"
        verbose_name_plural = "Conteúdos"

    def __str__(self):
        return f"{self.curso.nome} - {self.ordem}. {self.titulo}"
