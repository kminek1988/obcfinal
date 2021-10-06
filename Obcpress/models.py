from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=255, verbose_name='tytuł')
    paragraf1 = models.TextField()
    paragraf2 = models.TextField()
    paragraf3 = models.TextField()
    paragraf4 = models.TextField()
    paragraf5 = models.TextField()
    index = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    fotopress1 = models.ImageField(upload_to='media/press/', blank=True)
    fotopress2 = models.ImageField(upload_to='media/press/', blank=True)
    fotopress3 = models.ImageField(upload_to='media/press/', blank=True)
    fotopress4 = models.ImageField(upload_to='media/press/', blank=True)
    fotopress5 = models.ImageField(upload_to='media/press/', blank=True)
    created_at = models.DateTimeField(auto_now=True, verbose_name='dodany dnia', null=True, blank=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Artykuł'
        verbose_name_plural = 'Artykuły'
