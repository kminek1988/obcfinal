from django.shortcuts import render
from Obcpress.models import Articles

# Create your views here.
def Obcpress(request):
    art =  Articles.objects.all()
    context = {
        'art':art
    }
    return render(request, 'obcpress.html', context)