from django import forms
from .models import Reservation;

SERVICE_CHOICE = [
    ("Midi", "Midi"),
    ("Soir","Soir")
]

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        service = forms.ChoiceField(choices = SERVICE_CHOICE)
        fields = ['lastName', 'firstName', 'email', 'phone', 'date', 'tableSetNumber', 'service']
