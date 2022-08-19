"""Proyecto_supera URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
"""
from django.contrib import admin
from django.urls import path
from Proyecto_supera.views import inicio,probandoTemplate,probandoTemplate_loader
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Inicio/', inicio), # Muesta un mensaje de inicio (Se puede borrar)
    path('Template/', probandoTemplate),# Es solo de prueba para cargar un template (Se puede borrar)
    path('Template2/', probandoTemplate_loader), # Es solo de prueba para cargar un loader con un Template (Se puede borrar)
]
