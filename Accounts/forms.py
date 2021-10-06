from django import forms

from django.contrib.auth.forms import UserCreationForm
#category
from django.utils.translation import ugettext_lazy as _
from django.utils.html import mark_safe
from crispy_forms.helper import FormHelper
from crispy_forms import layout, bootstrap, helper

#moje

from Accounts.models import Profil, User
from Lists.models import Category, City
from  django.utils.safestring import  mark_safe

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RejestracjaForm(UserCreationForm):
    class Meta:
        model = User

        fields = [
            'username',
            'email',
            'password1',
            'password2',




        ]
class ProfileForm(forms.ModelForm):
    profilimg = forms.ImageField(widget=forms.FileInput,
                                 label = "Zdjęcie profilowe",
                                )
    port1 = forms.ImageField(widget=forms.FileInput,
                             label = "Zdjęcie nr 1"
                                )
    port2 = forms.ImageField(widget=forms.FileInput,
                             label = "Zdjęcie nr 2"
                                )
    port3 = forms.ImageField(widget=forms.FileInput,
                             label = "Zdjęcie nr 3"
                                )
    port4 = forms.ImageField(widget=forms.FileInput,
                             label = "Zdjęcie nr 4"
                                )
    port5 = forms.ImageField(widget=forms.FileInput,
                             label = "Zdjęcie nr 5"
                                )
    class Meta:
        model = Profil
        exclude = ['kategoria']


        fields = [

            'name',
            'surname',
            'profilimg',
            'description',
            'kategoria',
            'kod',
            'strona',
            'telefon',
            'profesja',
            'miasto',
            'port1',
            'port2',
            'port3',
            'port4',
            'port5',
            'typ',
            'status',
        ]

class kategoriaForm(forms.ModelForm):

    class Meta:
        model = Profil
        fields = ('kategoria', )



