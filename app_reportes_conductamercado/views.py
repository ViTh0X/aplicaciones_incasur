from django.http import HttpResponse
from django.shortcuts import render
from django.db import connections
from .forms import FechasComisionesGastosForm
import pandas as pd
# Create your views here.

def comisiones_gastos(request):
    if request.method == 'POST':
        form = FechasComisionesGastosForm(request.POST)
        if form.is_valid():
            fecha_inicio = form.cleaned_data['fecha_inicio']
            fecha_fin = form.cleaned_data['fecha_fin']
            query = "SELECT * FROM fxcomision_gastos(%s, %s);"
            with connections['dat-cierre'].cursor() as cursor:
                cursor.execute(query, [fecha_inicio, fecha_fin])
                data = cursor.fetchall()
                
                # Obtenemos los nombres de las columnas para que el DataFrame no quede solo con números
                columnas = [desc[0] for desc in cursor.description]
                
                # Creamos el DataFrame
                df = pd.DataFrame(data, columns=columnas)            
                df = df.rename(columns={
                    'cproducto': 'Cod.',
                    'tipoproducto': 'TIPO PROUCTO',
                    'ccategoria': 'Cod',
                    'categoriaconcepto': 'CATEGORIA O CONCEPTO',
                    'cdenomincacion': 'Cod',
                    'denominacion': 'DENOMINACION',
                    'moneda': 'MONEDA',
                    'periodicidad': 'PERIODICIDAD',
                    'tipocomisiongasto': 'TIPO COMISION o GASTO',
                    'porcenmin': 'PORCENTAJE MINIMO',
                    'porcenmax': 'PORCENTAJE MAXIMO',
                    'montomin': 'MONTO MINIMO',
                    'montomax': 'MONTO MAXIMO',
                })
                response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
                response['Content-Disposition'] = f'attachment; filename="ComisionesGastosde{fecha_inicio}-{fecha_fin}.xlsx"'
                df.to_excel(response,index=False,sheet_name='InventarioHardware')
                return response 
    else:
        form = FechasComisionesGastosForm()
    return render(request, 'reportes_conductamercado/comisiones_gastos.html', {'form': form})

def reporte_rr3(request):
    if request.method == 'POST':
        form = FechasComisionesGastosForm(request.POST)
        if form.is_valid():
            fecha_inicio = form.cleaned_data['fecha_inicio']
            fecha_fin = form.cleaned_data['fecha_fin']
            query = "SELECT * FROM fxBerenise(%s, %s);"
            with connections['dat-cierre'].cursor() as cursor:
                cursor.execute(query, [fecha_inicio, fecha_fin])
                data = cursor.fetchall()
                
                # Obtenemos los nombres de las columnas para que el DataFrame no quede solo con números
                columnas = [desc[0] for desc in cursor.description]
                
                # Creamos el DataFrame
                df = pd.DataFrame(data, columns=columnas)            
                df = df.rename(columns={
                    'ccodigo': 'Codigo',
                    'cdescri': 'Operaciones-Servicios-Productos',
                    'ccanal': 'Canal',
                    'cpernat': 'PersonaNatural', 
                    'cperjur': 'PersonaJuridica',                    
                })
                response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
                response['Content-Disposition'] = f'attachment; filename="ReporteRR3de{fecha_inicio}-{fecha_fin}.xlsx"'
                df.to_excel(response,index=False,sheet_name='InventarioHardware')
                return response 
    else:
        form = FechasComisionesGastosForm()
    return render(request, 'reportes_conductamercado/reporte_rr3.html', {'form': form})