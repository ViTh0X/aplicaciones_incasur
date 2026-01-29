from django.shortcuts import render

from django.http import HttpResponse

from utilidades.secreto_bancario1 import Secretobancario1
from .forms import formularioSubirExcel
from datetime import datetime
# Create your views here.
def generar_word_secban_legal(request):
    dia = datetime.now().day
    mes = datetime.now().month
    año = datetime.now().year
    mes_texto = ""
    if mes < 10:
        mes_texto = f"0{mes}"
    else:
        mes_texto = str(mes)
    
    dia_texto = ""
    if dia < 10:
        dia_texto = f"0{dia}"
    else:
        dia_texto = str(dia)
    if request.method == 'POST':
        formulario = formularioSubirExcel(request.POST, request.FILES)
        if formulario.is_valid():
            archivo_excel = request.cleaned_data['archivo_excel']
            correlativo = request.cleaned_data['numero_correlativo']
            secban = Secretobancario1(archivo_excel)
            secban.generar_word_2(dia,mes,año,correlativo)
            response = HttpResponse(sb.buffer.read(), content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
            response["Content-Disposition"] = f'attachment; filename="Levantamiento secreto bancario {dia_texto}-{mes_texto}.docx"'
            return response
    else:
        formulario = formularioSubirExcel()
    return render(request,'secretobancario_legal/secreto_bancario_legal.html',{'formulario':formulario})