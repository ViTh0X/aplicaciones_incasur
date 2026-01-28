from django import forms

class formularioSubirExcel(forms.Form):
    archivo_excel = forms.FileField(
        label='Subir el archivo excel generado',
    )