from django.db import models
from django.contrib.auth.models import User

class Professor(User):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    curriculo = models.TextField()
    formacao = models.CharField(max_length=255)

    def __str__(self):
        return self.user.get_full_name()
