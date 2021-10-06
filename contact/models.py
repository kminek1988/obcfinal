from django.db import models
from django.utils.translation import gettext_lazy
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete


from Accounts.models import Profil



# Create your models here.

class Contact (models.Model):
    name  = models.CharField(max_length=255, verbose_name='pseudonim', unique=True, null=False, blank=True, default="")
    imie = models.CharField(max_length=255, verbose_name='imię', null=True, blank=True)
    nazwisko = models.CharField(max_length=255, verbose_name='nazwisko', null=True, blank=True)
    miasto = models.CharField(max_length=255, verbose_name='miasto', null=True, blank=True)
    profesja = models.CharField(max_length=255, verbose_name='profesja', null=True, blank=True)
    owner =models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING)


    class Meta:
        verbose_name = 'kontakt'
        verbose_name_plural = 'kontakty'

    def __str__(self):
        return f'{self.name} {self.owner}'


