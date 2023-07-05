from django.db import models
from django.urls import reverse


# Create your models here.


class Configuration(models.Model):
    nom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100, blank=True)
    adresse = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to="Logo", blank=True, null=True)
    date_ajout = models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("confighotel:detail-config", kwargs={"pk": self.pk})

    def __str__(self):
        return self.nom


class Categories(models.Model):
    CLASSES_CHAMBRES = (
        ("Classe A", "classe A"),
        ("Classe B", "classe B"),
        ("Classe C", "classe C"),
        ("Classe VIP", "VIP")
    )
    categorie = models.CharField(max_length=150, choices=CLASSES_CHAMBRES)
    prix_enfant = models.FloatField(default=0.0)
    prix_adulte = models.FloatField(default=0.0)

    class Meta:
        verbose_name = ("Categorie")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.categorie