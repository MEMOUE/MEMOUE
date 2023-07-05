from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from resto.form import RestoForm
from resto.models import Restaurant


# Create your views here.
class CreateMenu(CreateView):
    form_class = RestoForm
    template_name = "resto/add_menu.html"

    success_url = "/resto"


class ListMenu(ListView):
    template_name = "resto/home_resto.html"
    queryset = Restaurant.objects.all()


class UpdateMenu(UpdateView):
    form_class = RestoForm
    template_name = "resto/add_menu.html"
    #queryset = Restaurant.objects.all()

    success_url = "/resto"

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Restaurant, id=id)


class DeleteMenu(DeleteView):
    template_name = "resto/delete.html"
    queryset = Restaurant.objects.all()

    success_url = "/resto"

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Restaurant, id=id)


def deleteMenu(request, id):
    obj = Restaurant.objects.get(id=id)
    pass