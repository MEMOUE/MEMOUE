from django.urls import path
from .views import chambre_view, liste_chambre

urlpatterns = [
    path('add/', chambre_view, name='chambre'),
    path('', liste_chambre, name='liste_chambre'),
]