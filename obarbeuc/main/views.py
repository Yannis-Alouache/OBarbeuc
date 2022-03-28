from django.shortcuts import render
from .models import TodayLunch


# Create your views here.
def HomeView(request):
    todayLunchs = TodayLunch.objects.all()
    context = {
        'todayLunchs' : todayLunchs
    }
    return render(request, "home.html", context)

def NotFoundView(request, exception):
    return render(request, "404.html")