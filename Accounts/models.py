from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.urls import reverse
from django.dispatch import receiver
from Lists.models import Category


class Profil (models.Model):
    TYP = (
        ('Szukający', 'Szukający'),
        ('Obrotny', 'Obrotny'),
    )
    STATUS = (
        ('Aktywny', 'Aktywny'),
        ('Nieaktywny', 'Nieaktywny'),
    )
    user = models.OneToOneField(User, default=None, null=True, on_delete=models.CASCADE)
    typ = models.CharField(choices=TYP, null=True, max_length=255, blank=True)
    name = models.CharField(max_length=255, verbose_name='imię', blank=True)
    surname = models.CharField(max_length=255, verbose_name='nazwisko', blank=True)
    description = models.TextField(verbose_name='opis', blank=True)
    profilimg = models.ImageField(upload_to='media/profiles/', blank=True, default='media/1.png')
    kategoria = models.ForeignKey(Category, verbose_name="Kategoria", null=True, blank=True,
                                  on_delete=models.DO_NOTHING)
    kod = models.DecimalField(max_digits=6, decimal_places=0, null=True, blank=True)
    strona = models.CharField(max_length=255, null=True, blank=True, default="np www.mojadomena.pl")
    telefon = models.CharField(max_length=50, null=True, blank=True, default="")
    profesja = models.CharField(max_length=50, null=True, blank=True, default="")
    miasto = models.CharField(max_length=50, null=True, blank=True, default="")
    port1 = models.ImageField(upload_to='media/portfolio/', blank=True, null=True, default='media/gwiazdka.png',
                              verbose_name="galeria zdjęcie nr 1")
    port2 = models.ImageField(upload_to='media/portfolio/', blank=True, null=True, default='media/gwiazdka.png',
                              verbose_name="galeria zdjęcie nr 2")
    port3 = models.ImageField(upload_to='media/portfolio/', blank=True, null=True, default='media/gwiazdka.png',
                              verbose_name="galeria zdjęcie nr 3")
    port4 = models.ImageField(upload_to='media/portfolio/', blank=True, null=True, default='media/gwiazdka.png',
                              verbose_name="galeria zdjęcie nr 4")
    port5 = models.ImageField(upload_to='media/portfolio/', blank=True, null=True, default='media/gwiazdka.png',
                              verbose_name="galeria zdjęcie nr 5")
    status =  models.CharField(choices=STATUS, default="Aktywny", max_length=255)
    black = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Profil"
        verbose_name_plural = "Profile"

    def __str__(self):
        return f'{self.user.username}'

    def get_absolute_url(self):
        return reverse('profil_view', args=[str(self.id)])


    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profil.objects.create(user=instance)
            instance.profil.save()


