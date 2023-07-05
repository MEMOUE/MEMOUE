from django.db import models

# Create your models here.
class Restaurant(models.Model):
    TYPE_MENU = (
        ("Boisson", "Boisson"),
        ("Plat Traditionnel", "Plat Traditionnel"),
        ("Plat Etranger", "Plat Etranger")
    )
    nom_menu = models.CharField(max_length=150)
    type = models.CharField(max_length=100, choices=TYPE_MENU)
    quantite = models.IntegerField(default=0)
    image = models.ImageField(upload_to="resto", blank=True, null=True)
    prix = models.FloatField(default=0.0)
    date = models.DateField(auto_now_add=True)
