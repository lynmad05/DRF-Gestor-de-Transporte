from django.db import models

class Conductor(models.Model):
    nombre = models.CharField(max_length=100)
    numero_licencia = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Ruta(models.Model):
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    conductor = models.ForeignKey(Conductor, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return f"{self.origen} - {self.destino}"
