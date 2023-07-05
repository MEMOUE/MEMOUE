from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model


class InscriptionForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ("username", "email", "first_name", "last_name",)

        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "password": forms.PasswordInput(attrs={"class": "form-control"})
        }


class ConnexionForm(AuthenticationForm):
   username = forms.CharField(max_length=100, label="Nom d'utilisateur", widget=forms.TextInput(attrs={"class": "form-control"}))
   password = forms.CharField(max_length=100, label="Mot de passe", widget=forms.PasswordInput(attrs={"class": "form-control"}))
