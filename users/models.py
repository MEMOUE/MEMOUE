from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Users(AbstractUser):
    image_profile = models.ImageField()

    def __str__(self):
        return self.first_name


class Personnel(models.Model):
    FONCTION_CHOICES = (
        ('receptionniste', 'Réceptionniste'),
        ('menagere', 'Ménagère'),
        ('caissiere', 'Caissier(e)'),
        ('responsable', 'Responsable'),
        ('stagiaire', 'Stagiaire'),
        ('autre', 'Autre'),
    )

    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    email = models.EmailField()
    mot_de_passe = models.CharField(max_length=100)
    adresse = models.CharField(max_length=200)
    fonction = models.CharField(max_length=100, choices=FONCTION_CHOICES)
    date_inscription = models.DateField(null=True)
    date_expiration = models.DateField(null=True)

    class Meta:
        verbose_name = ("Personnel")
        verbose_name_plural = ("Personnels")

    def __str__(self):
        return self.nom + ' ' + self.prenom