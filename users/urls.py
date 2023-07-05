from django.urls import path
from .views import inscription, connexion, deconnexion, home

urlpatterns = [
    path("inscription/", inscription, name="inscription"),
    path("connexion/", connexion, name="connexion"),
    path("home/", home, name="home-users"),
    path("deconnexion", deconnexion, name="deconnexion"),
]