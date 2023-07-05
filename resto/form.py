from django import forms

from resto.models import Restaurant


class RestoForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = "__all__"