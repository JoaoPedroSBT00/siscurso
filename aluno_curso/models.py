from django.db import models
from aluno.models import Aluno
from cursos.models import Curso

class AlunoCurso(models.Model):
    STATUS_CHOICES = [
        ('matriculado', 'Matriculado'),
        ('cursando', 'Cursando'),
        ('concluido', 'Concluído'),
        ('cancelado', 'Cancelado'),
        ('suspenso', 'Suspenso'),
    ]
    
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    dt_mat = models.DateField(verbose_name="Data de Matrícula")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='matriculado')

    class Meta:
        unique_together = ('aluno', 'curso')
        verbose_name = "Matrícula"
        verbose_name_plural = "Matrículas"

    def __str__(self):
        return f"{self.aluno.user.get_full_name()} - {self.curso.nome} ({self.status})"
