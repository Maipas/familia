from multiprocessing import context
from django.http import HttpResponse
from django.template import Template, Context
from datetime import datetime
from django.shortcuts import render

def saludo(request):
    return HttpResponse('buenas')

def index(request):
    return render(request, 'index.html')

def fecha(request):
    fecha=datetime.now().date()
    mensaje= f'hoy es {fecha}'
    return HttpResponse(mensaje)

def plantilla(request):
    context = {
        'nombre': 'Mauro',
        'apellido': 'Pasinato',
        'fecha':datetime.now()
    }
    return render(request, 'template_1.html', context = context)

# def plantilla(self):

#     miHtml = open("C:/Users/Maipa/Desktop/familia/mifamilia/template/template_1.html")
#     template = Template(miHtml.read())
#     miHtml.close()
#     miContexto = Context()
#     documento = template.render(miContexto)
#     return HttpResponse(documento)

