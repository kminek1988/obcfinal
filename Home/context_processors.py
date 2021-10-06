from Home.models import introFoto
from Home.forms import ContactMeForm
from Accounts.models import Profil
from django.db.models import Count
from django.contrib.auth.models import User

def aktufoto(request, id=None):
    allfoto = introFoto.objects.all()
    foto1 = introFoto.objects.filter(id=1)
    foto2 = introFoto.objects.filter(id=2)
    foto3 = introFoto.objects.filter(id=3)

    return {
        'allfoto': allfoto,
        'foto1' : foto1,
        'foto2' : foto2,
        'foto3' : foto3,
    }
def contactmeview(request):
    return {
        'contactmeform':ContactMeForm()
    }

def ile(request):
    ile = Profil.objects.filter(id__isnull=False).count()
    suma = print(ile)
    return {
        'ile': ile,
        'suma': suma,
    }