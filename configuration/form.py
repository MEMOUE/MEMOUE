from django import forms

from configuration.models import Configuration, Categories


class ConfigForm(forms.ModelForm):
    class Meta:
        model = Configuration
        fields = "__all__"

        widgets = {
            "nom": forms.TextInput(attrs={"class": "form-control m-2"}),
            "telephone": forms.TextInput(attrs={"class": "form-control m-2"}),
            "adresse": forms.TextInput(attrs={"class": "form-control m-2"})
        }


class ReglePrixForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = "__all__"

        widgets = {
            "categorie": forms.Select(attrs={"class": "form-select m-2"}),
            "prix_enfant": forms.NumberInput(attrs={"class": "form-control m-2"}),
            "prix_adulte": forms.NumberInput(attrs={"class": "form-control m-2"})
        }