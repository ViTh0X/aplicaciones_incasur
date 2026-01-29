from django.shortcuts import render
from django.http import HttpResponse

from utilidades.secreto_bancario1 import Secretobancario1
from .forms import formularioSubirExcel
import zipfile
from io import BytesIO

# Create your views here.
def generar_word_secban_ahorros(request):
    if request.method == 'POST':
        formulario = formularioSubirExcel(request.POST, request.FILES)
        if formulario.is_valid():
            archivo_excel = formulario.cleaned_data['archivo_excel']
            secban = Secretobancario1(archivo_excel)        
            secban.generar_word_1()
            zip_buffer = BytesIO()
            with zipfile.ZipFile(zip_buffer,"w") as zip_file:
                for filename, buffer in secban.buffers:
                    zip_file.writestr(filename,buffer.getvalue())
            zip_buffer.seek(0)
            response = HttpResponse(zip_buffer.getvalue(), content_type='application/zip')
            response["Content-Disposition"] = 'attachment; filename="SecretoBancario_Ahorros.zip"'
            return response
    else:
        formulario =  formularioSubirExcel()
    
    return render(request,'secretobancario_ahorros/secreto_bancario_ahorros.html',{'formulario':formulario})        
            
        