from django.shortcuts import render, get_object_or_404, redirect

from reservation.forms import ReservationForm
from reservation.models import Reservation


# Create your views here.


def reservation_view(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/liste_reservation')
    else:
        form = ReservationForm()
    return render(request, 'reservation/reservation.html', {'form': form})


def liste_reservation(request):
    reservations = Reservation.objects.all()
    context = {'reservations': reservations}
    return render(request, 'reservation/liste_reservation.html', context)


def modifier_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)

    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('liste_reservation')
    else:
        form = ReservationForm(instance=reservation)

    return render(request, 'reservation/modifier_reservation.html', {'form': form})


def supprimer_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)

    if request.method == 'POST':
        reservation.delete()
        return redirect('liste_reservation')

    return render(request, 'reservation/supprimer_reservation.html', {'reservation': reservation})