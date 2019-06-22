from django.db import models


class CadastraPresenca(models.Model):

    cpf = models.CharField(max_length=11)
    mac = models.CharField(max_length=17)
    coordenada = models.CharField(max_length=25)
    horario = models.DateTimeField(auto_now_add=True)
    presenca = models.BooleanField(default=False)


# Create your models here.
