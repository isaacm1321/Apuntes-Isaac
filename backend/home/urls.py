# importacio nes

from django.urls import path
from backend.home.views import home_inicio


urlpatterns = [
    path('', home_inicio)
]








