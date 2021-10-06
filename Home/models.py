from django.db import models

class introFoto(models.Model):
    title = models.CharField(max_length=255, verbose_name='tytuł')
    zdj = models.ImageField(upload_to='media/aktualnosci/', blank=True, null=True, default='media/1.jpg', verbose_name="aktualnosci1")
    class Meta:
        verbose_name = 'Zdjęcie w intro'
        verbose_name_plural = 'Zdjęcia w intro'
    def __str__(self):
        return self.title

class Faq(models.Model):
    TEMAT = (
        ('Problemy Techniczne','Problemy Techniczne'),
        ('Współpraca', 'Współpraca'),
        ('Promocja i Reklama', 'Promocja i Reklama'),
        ('Wydarzenia i imprezy', 'Wydarzenia i imprezy'),
    )
    name = models.CharField(max_length=255, verbose_name='Z kim mamy przyjemność?')
    email = models.EmailField()
    subject = models.CharField(choices=TEMAT, max_length=255, verbose_name='temat')
    date = models.DateTimeField(auto_now_add=True, verbose_name='data')
    message=models.TextField(verbose_name='Treść wiadomości')

    def __str__(self):
        return f'{self.name} {self.email} {self.subject}{self.date}{self.message}'