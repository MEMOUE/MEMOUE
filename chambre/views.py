from django.shortcuts import render, redirect
from .forms import ChambreForm
from .models import Chambre
# Create your views here.


def chambre_view(request):
    if request.method == 'POST':
        form = ChambreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/liste_chambre')
    else:
        form = ChambreForm()
    return render(request, 'chambre/chambre.html', {'form': form})



def liste_chambre(request):
    chambre = Chambre.objects.all()
    return render(request, 'chambre/liste_chambre.html', {'chambres': chambre})