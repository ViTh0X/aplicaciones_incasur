from django import forms

class formularioSubirExcel(forms.Form):
    archivo_excel = forms.FileField(
        label='Suba el archivo excel generado',
    )    
    numero_correlativo = forms.IntegerField(
        label='Ingrese el correlativo',
        required=True
    )