from django.db import models

# Create your models here.


class Chambre(models.Model):
    numero_chambre = models.CharField(max_length=10, null=True, unique=True)
    TYPE_CHOICES = [
        ('simple', 'Simple'),
        ('double', 'Double'),
    ]
    ETAT_CHOICES = [
        ('libre', 'Libre'),
        ('occupee', 'Occupée'),
    ]
    type_chambre = models.CharField(max_length=10, null=True, choices=TYPE_CHOICES)
    STATUT_CHOICES = [
        ('sale', 'Sale'),
        ('propre', 'Propre'),
    ]
    statut = models.CharField(max_length=10, null=True, choices=STATUT_CHOICES)
    etat = models.CharField(max_length=10, null=False, choices=ETAT_CHOICES)
    prix = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField(null=True)