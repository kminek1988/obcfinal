
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError, EmailMessage, get_connection
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.core.mail import send_mail

from Home.forms import ContactMeForm, szukajkaForm
from Home.models import Faq

# Create your views here.

class Home(TemplateView):
   template_name = 'home.html'

def rodo(request):
   return render(request, "rodo.html")

def polityka(request):
   return render(request, "polityka.html")

def regulamin(request):
   return render(request, "regulamin.html")


def contactmeView(request):
   contactmeform = ContactMeForm(request.POST)


   if request.method == 'POST':
      if contactmeform.is_valid():
       contactmeform.save() # form.save()
      my_host = 'mail.privateemail.com'
      my_port= 587
      my_username = 'faq@obrotni.de'
      my_password = 'klopik007'
      my_use_tls = True

      form_detail = Faq.objects.last()
      message = str(form_detail)
      connection = get_connection(host=my_host,
                                  port=my_port,
                                  username=my_username,
                                  password=my_password,
                                  use_tls=my_use_tls)
      send_mail(
         'Nowe Zapytanie',
         message,
         'faq@obrotni.de',
         ['admin@obrotni.de'],
         connection=connection,
         fail_silently=False,
      )

      return render(request, 'sukces.html')
   else:
      contactmeform = ContactMeForm(request.POST)
      context = {'contactmeform': contactmeform}
      return render(request, 'formularz.html', context)

def successView(request):
   return render(request, 'sukces.html')

def szukajka(request):
   template_name = 'search.html'
   context = {
      'form': szukajkaForm
   }
   return render(request, 'search/search.html', context)