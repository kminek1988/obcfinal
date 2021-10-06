from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RejestracjaForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from Accounts.models import Profil

#do rejestracji użytkownika
from django.contrib.auth import get_user_model

from django.shortcuts import render

from Accounts.forms import RejestracjaForm, ProfileForm, kategoriaForm

from Lists.models import City, Category


UserModel = get_user_model(),

# Create your views here.
def test (request):
    return render(request, 'potwierdz.html')
def signup(request):
    if request.method == 'POST':
        form = RejestracjaForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Aktywacja konta.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return  render(request, 'potwierdz.html')
    else:
        form = RejestracjaForm()
    return render(request, 'rejestracja.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

@login_required
def Edycja(request):
    if request.method == 'POST':

        form = ProfileForm(request.POST, request.FILES, instance=request.user.profil)  # request.FILES is show the selected image or file


        if form.is_valid():
            form.save()

            return redirect('profil')
    else:

        form = ProfileForm(instance=request.user.profil)

    return render(request, 'edit_profil.html', {'form':form})

@login_required
def miasto_list_edit(request):
    a = City.objects.filter(letter='A')
    aa = City.objects.filter(letter='Ä')
    b = City.objects.filter(letter='B')
    c = City.objects.filter(letter='C')
    d = City.objects.filter(letter='D')
    e = City.objects.filter(letter='E')
    f = City.objects.filter(letter='F')
    g = City.objects.filter(letter='G')
    h = City.objects.filter(letter='H')
    i = City.objects.filter(letter='I')
    j = City.objects.filter(letter='J')
    k = City.objects.filter(letter='K')
    l = City.objects.filter(letter='L')
    m = City.objects.filter(letter='M')
    n = City.objects.filter(letter='N')
    o = City.objects.filter(letter='O')
    oo = City.objects.filter(letter='Ö')
    p = City.objects.filter(letter='P')
    r = City.objects.filter(letter='R')
    s = City.objects.filter(letter='S')
    t = City.objects.filter(letter='T')
    u = City.objects.filter(letter='U')
    uu = City.objects.filter(letter='Ü')
    w = City.objects.filter(letter='W')
    x = City.objects.filter(letter='X')
    y = City.objects.filter(letter='Y')
    z = City.objects.filter(letter='Z')

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
    return render(request, 'city_list_edit.html', context)

@login_required
def kategoria_list_edit(request, id):

    profil = Profil.objects.filter(id=id)
    miasto = City.objects.filter(id=id)
    kategoria = Category.objects.filter(city__in=miasto)


    if request.method == 'POST':
        drop = request.POST.get('droping')
        kat = Category.objects.get(id=drop)
        request.user.profil.kategoria = kat
        request.user.profil.save()


    context = {

        'profil': profil,
        'miasto': miasto,
        'kategoria': kategoria,



    }

    return render(request, 'kat.html', context)









@login_required
def profil(request, pk=None):
    opis = request.user.profil
    context = {'opis': opis,

               }
    return render(request, 'profil.html', context)


def style(request):
    return render(request, 'accounts/confirm.html')