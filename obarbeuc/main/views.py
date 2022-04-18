from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.core.mail import send_mail

from reservation.models import Reservation
from .models import TodayLunch
from .forms import CovidForm
from datetime import datetime
import os

# Create your views here.
def HomeView(request):
    todayLunchs = TodayLunch.objects.all()
    context = {
        'todayLunchs' : todayLunchs
    }
    return render(request, "home.html", context)

def NotFoundView(request, exception):
    return render(request, "404.html")

def rgpdView(request):
    try:
        with open(os.path.abspath(os.curdir) + "/static/files/rgpd.pdf", 'rb') as f:
            return HttpResponse(f.read(), content_type="application/pdf")
    except IOError:
        raise Http404

@login_required
def CovidView(request):
    context = {}
    if request.method == 'POST':
        form = CovidForm(request.POST)
        context['form'] = form
        if form.is_valid():
            verifForm = form.save(commit=False)
            verifForm.user = request.user
            if date_valid(verifForm.date) is not True:
                context['message_failure'] = "Date Invalide"
                return render(request, 'covid.html', context)
            if reserved(verifForm) is True:
                cas_contacts = Reservation.objects.filter(date=verifForm.date, service=verifForm.service).exclude(email=verifForm.user.email)
                for people in cas_contacts:
                    send_mail("Cas Contact Obarbeuc", "Bonjour, \nSuite à votre visite dans notre restaurant l'un des clients à attraper la COVID vous êtes donc cas contact nous vous conseillons de vous faire tester au plus vite.", None, [people.email], fail_silently=False)
                form.save()
                context['message_success'] = "Un mail à était envoyé à tous les cas contact"
                return render(request, 'covid.html', context)
            else:
                context['message_failure'] = "Vous n'avez pas réserver à la date indiqué"
                return render(request, 'covid.html', context)
    else:
        context['form'] = CovidForm()
    return render(request, "covid.html", context)


def reserved(form):
    reservation = Reservation.objects.filter(date=form.date, service=form.service, email=form.user.email)
    if reservation.__len__() <= 0:
        return False
    return True

def date_valid(reservationDate):
    today = datetime.strptime(datetime.today().strftime("%Y-%m-%d"), "%Y-%m-%d").date()
    if reservationDate <= today:
        return True
    return False