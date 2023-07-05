from django.shortcuts import render


# Create your views here.
def home_stat(request):
    return render(request, "statistique/home_stat.html")