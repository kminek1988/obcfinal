from django.urls import path, include
from Home.views import Home, rodo, polityka, regulamin, contactmeView, successView

urlpatterns = [

    path('', Home.as_view(), name='homepage' ),
    path('rodo/', rodo, name='rodo'),
    path('polityka/',polityka, name='polityka'),
    path('regulamin/',regulamin, name='regulamin'),
    path('formularz/', contactmeView, name='kontakt'),
    path('success/', successView, name='success'),
]