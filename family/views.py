from django.shortcuts import render
from family.models import Family

# Create your views here.
def family(request):
        familiares = Family.objects.all()
        context = {'familiares': familiares}
        return render(request, 'family.html', context = context)

# def family(request):
#         familiar_nuevo = Family.objects.create(
#                 nombre = 'Augusto', 
#                 apellido='Pasinato', 
#                 nacimiento = '08191976', 
#                 edad= 45, 
#                 estado= 'casado', 
#                 parentesco='Primo' )
#         context = {'familiar_nuevo': familiar_nuevo}
#         return render(request, 'family.html', context = context)
