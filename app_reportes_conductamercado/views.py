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
            df = pd.read_sql_query(query, connections['dat-cierre'], params=[fecha_inicio, fecha_fin])
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
    return render(request, 'app_reportes_conductamercado/comisiones_gastos.html', {'form': form})