from django import forms
from .models import Country, Location

class Country(forms.ModelForm):
    class Meta:
        model = Country
        fields = "__all__"


class Location(forms.ModelForm):
    class Meta:
        model = Location
        fields = "__all__"
