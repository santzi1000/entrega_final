from django.db import models


class Proceso(models.Model):
    name = models.CharField(max_length=40)
    tipe = models.CharField(max_length=40)
    email = models.EmailField()
    radicado = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.name} {self.tipe}"