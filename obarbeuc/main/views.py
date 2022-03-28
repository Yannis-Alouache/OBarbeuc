from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import TodayLunch
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