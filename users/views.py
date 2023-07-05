from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .formulaire import InscriptionForm, ConnexionForm

# Create your views here.


def inscription(request):
    form = InscriptionForm()
    if request.method == "POST":
        form = InscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("connexion")
        else:
            form = InscriptionForm()
    return render(request, "users/inscription.html", context={"form":form})


def connexion(request):
    form = ConnexionForm()
    message = ""
    if request.method == "POST":
        form = ConnexionForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
            if user is not None and user.is_active and user.is_staff:
                login(request, user)
                return redirect("admin:index")
            else:
                login(request, user)
                return redirect("home-users")
        else:
            message = "Erreur d'identification"
    return render(request, "users/connexion.html", context={"form":form, "message":message})


@login_required
def home(request):
    return render(request, "users/home.html")


@login_required
def deconnexion(request):
    logout(request)
    return redirect("index")