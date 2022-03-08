from django.shortcuts import render

# Create your views here.
def RegisterView(request):
    return render(request, 'register.html', {})


def LoginView(request):
    return render(request, 'login.html', {})
