from django.shortcuts import render

from .models import TodayLunch

MAX_TABLE = 35

# Create your views here.
def HomeView(request):
    todayLunchs = TodayLunch.objects.all()
    context = {
        'todayLunchs' : todayLunchs
    }
    return render(request, "home.html", context)