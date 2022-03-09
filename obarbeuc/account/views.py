from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegisterForm

# Create your views here.
def RegisterView(request):
    context = {}
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_passord = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_passord)
            login(request, account)
            print("==========  COMPTE CREER SUUUUUUUUUUUUUUUUUUUUUUU   ==========")
            redirect('home')
        else:
            context['form'] = form
    else:
        form = RegisterForm()
        context['form'] = form
    return render(request, 'register.html', {'form' : form})


def LoginView(request):
    return render(request, 'login.html', {})
