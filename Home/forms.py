from django import forms
from Home.models import Faq
from haystack.forms import SearchForm

class ContactMeForm(forms.ModelForm):
    class Meta:
        model = Faq
        exclude = ['date']

        field = [
            'name',
            'email',
            'subject',
            'message',
        ]

class szukajkaForm(SearchForm):
    pass
