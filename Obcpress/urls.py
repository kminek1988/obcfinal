from django.urls import path, include
from Obcpress.views import Obcpress
urlpatterns = [
    path('obcpress/', Obcpress, name='obcpress'),

]