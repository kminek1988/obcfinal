from django.urls import path

from Lists.views import CityView, KategoriaView, ProfilView, Prof_detail



urlpatterns = [

    path('miasta/', CityView, name='miasta'),
    path('miasta/<int:pk>', KategoriaView, name='city_detail'),
    path ('kategoria/<int:pk>', ProfilView, name='kategoria_detail'),
    path('profil/<int:id>', Prof_detail, name='profil_view'),




]

