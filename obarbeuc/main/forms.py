from django import forms
from .models import CovidList;

SERVICE_CHOICE = [
    ("Midi", "Midi"),
    ("Soir","Soir")
]

class CovidForm(forms.ModelForm):
    class Meta:
        model = CovidList
        service = forms.ChoiceField(choices = SERVICE_CHOICE)
        fields = ['date', 'service']