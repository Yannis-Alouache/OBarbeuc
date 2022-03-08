from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.conf import settings

from .models import TodayLunch

MAX_TABLE = 35

# Create your views here.
def HomeView(request):
    todayLunchs = TodayLunch.objects.all()
    context = {
        'todayLunchs' : todayLunchs
    }
    return render(request, "home.html", context)