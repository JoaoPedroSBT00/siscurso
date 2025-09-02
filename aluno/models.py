import random
from django.db import models
from django.contrib.auth.models import User

def gerar_matricula():
    return str(random.randint(10000000, 99999999))  # 8 dígitos aleatórios

class Aluno(User):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    matricula = models.CharField(max_length=20, unique=True, default=gerar_matricula, editable=False)
    data_nascimento = models.DateField()

    def __str__(self):
        return f"{self.user.get_full_name()} ({self.matricula})"
