from django.urls import path

from reservation.views import reservation_view, modifier_reservation, supprimer_reservation, liste_reservation

urlpatterns = [
    path('add/', reservation_view, name='add_reservation'),
    path('modifier_reservation/<int:reservation_id>/', modifier_reservation, name='modifier_reservation'),
    path('supprimer_reservation/<int:reservation_id>/', supprimer_reservation, name='supprimer_reservation'),
    path('', liste_reservation, name='liste_reservation'),
]