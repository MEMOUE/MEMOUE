from django.urls import path
from .views import home_stat

urlpatterns = [
    path("", home_stat, name="home-stat"),
]