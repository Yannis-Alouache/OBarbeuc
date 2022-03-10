from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import Account

class RegisterForm(UserCreationForm):
    email = forms.EmailField(error_messages={'required': 'Entrez votre E-mail', 'invalid': 'email non valide'})
    phone = forms.RegexField(regex=r'^((\+)33|0)[1-9](\d{2}){4}$', error_messages={'invalid': 'téléphone non valide'})

    class Meta:
        model = Account
        fields = ('email', 'first_name', 'last_name', 'phone', 'password1', 'password2')

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            self.add_error('password2', "Les mots de passe ne sont pas identique")