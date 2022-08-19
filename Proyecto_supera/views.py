#Esta carpeta la podemos borrar. 
from django.template import Template , Context
from django.http import HttpResponse 
from django.template import loader

def inicio(request): # ESTA VISTA SE PUEDE BORRAR 
    return HttpResponse("Hola esta es una pantalla de prueba!")


def probandoTemplate(request): # ESTA VISTA SE PUEDE BORRAR ESTA ASOCIADA AL TEMPLATE DE LA CARPETA PROYECTO 

    miHTML= open("C:/Users/valen/OneDrive/Desktop/ProyectoFinal/Proyecto1/Proyecto_supera/plantillas/templates1.html")

    plantilla = Template(miHTML.read())

    miHTML.close()

    miContexto = Context()

    documento =  plantilla.render(miContexto)

    return HttpResponse(documento)


def probandoTemplate_loader(request): #ESTA VISTA SE PUEDE BORRAR ESTA ASOCIADA AL TEMPLATE DE LA CARPETA PROYECTO

    plantilla = loader.get_template("templates2.html")

    documento = plantilla.render()

    return HttpResponse(documento)
