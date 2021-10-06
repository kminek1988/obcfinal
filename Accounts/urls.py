from django.urls import path, include

from Accounts.views import  Edycja, profil, miasto_list_edit, kategoria_list_edit, signup, activate
from . import views
urlpatterns = [
    # auth + reset hasła

    path('edycja/', Edycja, name='edycja'),
    path('profil/', profil, name="profil"),
    path('miasto_list_edit/', miasto_list_edit, name='miasto_edit'),
    path('miasto_list_edit/<int:id>', kategoria_list_edit, name='kategoria_edit'),
    path('signup/', signup, name='rejestracja'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', activate, name='activate'),
    path ('test/', views.test),
    #
    # # aktywacja konta
    # path('verification/', include('verify_email.urls')),
    # path('activate/<uidb64>/<token>/', activate, name='activate'),

]