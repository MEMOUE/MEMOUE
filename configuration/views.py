from django.forms import formset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView, DetailView, ListView

from configuration.form import ConfigForm, ReglePrixForm
from configuration.models import Configuration, Categories


# Create your views here.


def home_config(request):
    return render(request, "confighotel/home.html")


def regle_prix(request):
    #ReglePrixFormset = formset_factory(ReglePrixForm, extra=4)
    #formset = ReglePrixFormset()
    form = ReglePrixForm()
    if request.method == "POST":
        form = ReglePrixForm(request.POST)
        #formset = ReglePrixFormset(request.POST or None)
        #formset = ReglePrixFormset(request.POST or None)
        #for form in formset:
        if form.is_valid():
            form.save()
            return redirect("confighotel:home-config")
    return render(request, "confighotel/create_rules.html", context={"form": form})


def update_rule(request, id):
    obj = get_object_or_404(Categories, id=id)
    if request.method == "POST":
        form = ReglePrixForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("confighotel:list-rule")
    else:
        form = ReglePrixForm(instance=obj)

    return render(request, "confighotel/update_rule.html", {"form": form})


def delete_rule(request, id):
    regle = get_object_or_404(Categories, id=id)
    if request.method == "POST":
        regle.delete()
        return redirect("confighotel:list-rule")
    return render(request, "confighotel/delete_rule.html")


class CreateConfig(CreateView):
    form_class = ConfigForm
    template_name = "confighotel/add.html"
    queryset = Configuration.objects.all()

    # success_url = "home-config"

    def form_valid(self, form):
        return super().form_valid(form)


class ListConfig(ListView):
    template_name = "confighotel/list_config.html"
    queryset = Configuration.objects.all()


class ListRegle(ListView):
    template_name = "confighotel/list_regle.html"
    queryset = Categories.objects.all()


class DetailConfig(DetailView):
    template_name = "confighotel/detail_config.html"
    queryset = Configuration.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Configuration, pk=id_)


class UpdateConfig(UpdateView):
    form_class = ConfigForm
    template_name = "confighotel/add.html"
    queryset = Configuration.objects.all()


def update_config(request):
    last = Configuration.objects.all().count()
    obj = Configuration.objects.get(id=last)
    form = ConfigForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("confighotel:detail-config")
    return render(request, "confighotel/add.html", {"form": form})



