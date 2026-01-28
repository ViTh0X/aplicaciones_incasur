from django.shortcuts import render

# Create your views here.
def home_opciones(request):
    return render(request,'home_opciones/listado_opciones.html')