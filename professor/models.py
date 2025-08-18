from django.db import models

class Professor(models.Model):
    formacao = models.CharField(max_length=100)

    def _str_(self):
        return self.formacao