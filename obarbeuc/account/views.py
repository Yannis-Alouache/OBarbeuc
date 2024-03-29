from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, LoginForm

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
            context['form'] = form
            context['message'] = f'Compte crée, Bienvenue {account.first_name}'
            return render(request, 'register.html', context)
        else:
            context['form'] = form
            print(form.error_messages)
    else:
        form = RegisterForm()
        context['form'] = form
    return render(request, 'register.html', {'form' : form})


def LoginView(request):
    context = {}
    if request.method == 'POST':
        form = LoginForm(request.POST)
        context['form'] = form
        if form.is_valid():
            user = authenticate(
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"]
            )
            if user is not None:
                login(request, user)
                context['messageSuccess'] = f'Bonjour {user.first_name} ! Vous êtes connecté'
                return render(request, 'login.html', context)
            else:
                context['messageFail'] = "Erreur de connexion"
                return render(request, 'logIn.html', context)
    else:
        context['form'] = LoginForm()
    return render(request, 'logIn.html', context)

def LogoutView(request):
    logout(request)
    return redirect('home')
