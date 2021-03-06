"""obarbeuc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from main.views import HomeView, rgpdView, CovidView
from account.views import RegisterView, LoginView, LogoutView
from reservation.views import ReservationView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView, name="home"),
    path('inscription', RegisterView, name="register"),
    path('connexion', LoginView, name="login"), 
    path('deconnexion', LogoutView, name="logout"),
    path('reservation', ReservationView, name="reservation"),
    path('rgpd', rgpdView, name="rgpd"),
    path('covid', CovidView, name="covid")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = "main.views.NotFoundView"