"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
    
    
    ! SE PODRIA DECIR QUE ESTE ES EL PRINCIPAL
    
    
"""
from django.contrib import admin
from django.urls import (
    path,
    include,
    ) # Es agregar la funcion como lo hariamos en la siguiente linea.
# from django.urls import include # ! Esta es la funcion que vamos a utilizar.



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')), # Agregando el paquete de rutas de la nueva aplicacion
]
