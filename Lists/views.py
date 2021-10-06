from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from django.db.models import Q
from django.contrib.auth.models import User
from Lists.models import City, Category
from Accounts.models import  Profil


#paginator
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


########################################################
# Lista wszystkich miast###################
def CityView(request):
    a= City.objects.filter(letter='A')
    aa= City.objects.filter(letter='Ä')
    b= City.objects.filter(letter='B')
    c= City.objects.filter(letter='C')
    d= City.objects.filter(letter='D')
    e= City.objects.filter(letter='E')
    f= City.objects.filter(letter='F')
    g= City.objects.filter(letter='G')
    h= City.objects.filter(letter='H')
    i= City.objects.filter(letter='I')
    j= City.objects.filter(letter='J')
    k= City.objects.filter(letter='K')
    l= City.objects.filter(letter='L')
    m= City.objects.filter(letter='M')
    n= City.objects.filter(letter='N')
    o= City.objects.filter(letter='O')
    oo= City.objects.filter(letter='Ö')
    p= City.objects.filter(letter='P')
    r= City.objects.filter(letter='R')
    s= City.objects.filter(letter='S')
    t= City.objects.filter(letter='T')
    u= City.objects.filter(letter='U')
    uu= City.objects.filter(letter='Ü')
    w= City.objects.filter(letter='W')
    x= City.objects.filter(letter='X')
    y= City.objects.filter(letter='Y')
    z= City.objects.filter(letter='Z')

    context = {
        'a': a,
        'b': b,
        'c': c,
        'd': d,
        'e': e,
        'f': f,
        'g' :g,
        'h': h,
        'i':i,
        'j': j,
        'k': k,
        'l': l,
        'm': m,
        'n':n,
        'oo':oo,
        'p':p,
        'r':r,
        's':s,
        't':t,
        'u': u,
        'uu': uu,
        'o': o,
        'w':w,
        'x':x,
        'y':y,
        'z':z,



        }
    return  render(request, 'CityView.html', context)

def KategoriaView(request, pk):
    miasto = City.objects.filter(pk=pk)
    kategoria = Category.objects.filter(city__in=miasto)



    context = {
        'miasto': miasto,
        'kategoria': kategoria,

    }
    return render(request, 'kategoriaView.html', context)

def ProfilView(request, pk):
    miasto = City.objects.filter(pk=pk)
    kategoria = Category.objects.filter(pk=pk)
    profil = Profil.objects.filter(kategoria__in=kategoria)

    context ={
        'miasto': miasto,
        'kategoria': kategoria,
        'prof': profil,
    }
    return render(request, 'prof.html',context)

def Prof_detail(request, id):
    profil = get_object_or_404(Profil, id=id)

    args = {
        'profil' : profil,
    }
    return render(request, 'profil_widok.html', args)
