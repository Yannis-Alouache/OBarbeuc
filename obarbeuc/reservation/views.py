from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ReservationForm
from datetime import datetime
from .models import Reservation
# Create your views here.


MAX_TABLE = 75

def get_remaining_table(reservations):
    compt = 0
    for i in range (0, len(reservations)):
        compt = compt + reservations[i].table
    return MAX_TABLE - compt

def date_valid(reservationDate):
    today = datetime.strptime(datetime.today().strftime("%Y-%m-%d"), "%Y-%m-%d").date()
    if reservationDate < today:
        return False
    return True

def table_valid(reservation):
    reservations = Reservation.objects.filter(date=reservation.date, service=reservation.service)
    remaining_table = get_remaining_table(reservations)

    print("Nombre de table restante", remaining_table)
    print("Nombre de table voulue ", rese&rvation.table)

    if remaining_table < reservation.table:
        return False
    return True


@login_required
def ReservationView(request):
    context = {}
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        context['form'] = form
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.table = round(reservation.tableSetNumber / 2)
            if date_valid(reservation.date) is not True:
                context['message_failure'] = "Date Invalide"
                return render(request, 'reservation.html', context)
            try:
                if table_valid(reservation) is True:
                    form.save()
                    context['message_success'] = "Reservation réussi !"
                    return render(request, 'reservation.html', context)
                else:
                    context['message_failure'] = "Il reste actuellement " + str(reservation.table) + " table pour le service demandé"
                    return render(request, 'reservation.html', context)
            except Reservation.DoesNotExist:
                form.save()
                context['message_success'] = "Reservation réussi !"
                return render(request, 'reservation.html', context)
    else:
        form = ReservationForm()
        context['form'] = form
    return render(request, "reservation.html", context)