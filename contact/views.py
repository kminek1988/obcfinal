from django.shortcuts import render
from django.contrib import messages
from contact.models import Contact
from django.utils.translation import get_language
from Accounts.models import Profil
from contact.forms import ContactForm


# Create your views here.

def add_or_change_contact(request, username=None):





    if request.method == 'POST':
        form = ContactForm(request.POST)
        user = request.user
        if form.is_valid():
            new_coment = form.save(commit=False)
            new_coment.owner = user
            new_coment.save()
            messages.success(request, 'kontakt został dodany do twojego notatnika')
            #form.save()
        return render(request, 'sukces1.html')
    else:
        form = ContactForm(request.POST)
        context = {'form':form }
        return render(request, 'ContactForm.html', context)
def delete_contact(request, pk):
    contact = Contact.objects.filter(pk=pk).delete()
    return render(request, 'sukces_delete.html')
