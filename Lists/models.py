from django.db import models
from django.urls import reverse


class City(models.Model):
    LITERA = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F','F'),
        ('G', 'G'),
        ('H', 'H'),
        ('I', 'I'),
        ('J', 'J'),
        ('K','K'),
        ('L', 'L'),
        ('M', 'M'),
        ('N', 'N'),
        ('O', 'O'),
        ('P', 'P'),
        ('R','R'),
        ('S', 'S'),
        ('T', 'T'),
        ('U','U'),
        ('W', 'W'),
        ('V','V'),
        ('Z','Z'),
        ('Ö','Ö'),
        ('Ä','Ä'),
        ('Ü','Ü'),
    )
    LAND = (
        ('Bawaria', 'Bawaria'),
        ('Baden', 'Badenia-Wirtembergia'),
        ('Hesja', 'Hesja'),
        ('Brandenburgia', 'Brandenburgia'),
        ('Brema', 'Brema'),
        ('Dolna', 'Dolna-Saksonia'),
        ('Maklemburgia', 'Meklemburgia Pomorze-Przednie'),
        ('NadreniaPl', 'Nadrenia Północna-Westfalia'),
        ('Saksonia', 'Saksonia'),
        ('Nadrenia', 'Nadrenia-Palatynat'),
        ('Saara', 'Saara'),
        ('SaksoniaAn', 'Saksonia-Anhalt'),
        ('Szlezwik', 'Szlezwik-Holsztyn'),
        ('Turyngia', 'Turyngia'),
    )
    title = models.CharField(max_length=255, verbose_name='nazwa')
    letter = models.CharField(max_length=1, choices=LITERA, verbose_name='litera')
    land = models.CharField(choices=LAND, max_length=255)

    class Meta:
        verbose_name = 'Miasto'
        verbose_name_plural = 'Miasta'
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('city_detail', kwargs={'pk':self.pk})

class Category(models.Model):
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING, verbose_name='miasto')
    title = models.CharField(max_length=255, verbose_name='nazwa')
    opis = models.TextField(blank=True)
    ikona = models.ImageField(upload_to='media/kategorie/', blank=True, default='media/1.png')
    class Meta:
        verbose_name = 'Kategoria'
        verbose_name_plural = 'Kategorie'
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('kategoria_detail', kwargs={'pk':self.pk})


