
from django.urls import path

from contact.views import delete_contact, add_or_change_contact


urlpatterns = [
    path('nowy/', add_or_change_contact, name='nowy'),
    path('kontakt-delete/', delete_contact, name="delete_contact"),





]

