from django import forms

from reservation.models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['date_reservation', 'date_arrivee', 'nombre_heures', 'nombre_jours']
        widgets = {
            'date_reservation': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date de réservation'}),
            'date_arrivee': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date d\'arrivée'}),
            'nombre_heures': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre d\'heures'}),
            'nombre_jours': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de jours'}),
        }
        error_messages = {
            'date_reservation': {
                'required': "Veuillez fournir une date de réservation.",
                'invalid': "Veuillez fournir une date valide pour la réservation.",
            },
            'date_arrivee': {
                'required': "Veuillez fournir une date d'arrivée.",
                'invalid': "Veuillez fournir une date valide pour l'arrivée.",
            },
            'nombre_heures': {
                'required': "Veuillez fournir le nombre d'heures.",
                'invalid': "Veuillez fournir un nombre valide pour les heures.",
            },
            'nombre_jours': {
                'required': "Veuillez fournir le nombre de jours.",
                'invalid': "Veuillez fournir un nombre valide pour les jours.",
            },
        }