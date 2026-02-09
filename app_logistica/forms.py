from django import forms
from .models import *
#from django.forms import PasswordInput

class Login_Formulario(forms.Form):
    usuario = forms.CharField(required=True,widget=forms.TextInput(attrs={'autocomplete':'off'}))
    password = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'autocomplete':'off'}))
    
class AlmacenesForm(forms.ModelForm):
    
    class Meta:
        model = Almacenes
        fields = ['nombre_almacen','descripcion_almacen','direccion_almacen']
    



    
    