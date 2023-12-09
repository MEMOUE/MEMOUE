from django.db import models

# Create your models here.


class Reservation(models.Model):
    date_reservation = models.DateField(null=True)
    date_arrivee = models.DateField(null=True)
    nombre_heures = models.IntegerField(null=True)
    nombre_jours = models.IntegerField(null=True)
