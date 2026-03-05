from django import forms
from .models import *

class ProyectosForm(forms.ModelForm):
    class Meta:
        model = Proyectos
        fields = ['nombre_proyecto','detalle_proyecto']
        
        
class TareasForm(forms.ModelForm):
    class Meta:
        model = Tareas
        fields = ['detalle_tarea']
    
class SubtareaForm(forms.ModelForm):
    class Meta:
        model = SubTareas
        fields = ['detalle_subtarea','inicio_actividad','fin_actividad','responsable_asignado']
        widgets = {
            'inicio_actividad': forms.DateInput( 
                format='%d-%m-%Y', #Para que al momento de editar me muestre en ese formato mis datos              
                attrs={'type':'date'}
            ),
            'fin_actividad': forms.DateInput(                
                format='%d-%m-%Y', 
                attrs={'type':'date'}
            ),
        }
        
        
class SubtareaEditForm(forms.ModelForm):
    class Meta:
        model = SubTareas
        fields = ['detalle_subtarea','inicio_actividad','fin_actividad','responsable_asignado','estado_tareas']
        widgets = {
            'inicio_actividad': forms.DateInput( 
                format='%Y-%m-%d', #Para que al momento de editar me muestre en ese formato mis datos              
                attrs={'type':'date'}
            ),
            'fin_actividad': forms.DateInput(                
                format='%Y-%m-%d', 
                attrs={'type':'date'}
            ),
        }
        
        
class  GestionSubtareaForm(forms.ModelForm):
    class Meta:
        model = GestionSubtareas
        fields = ['detalle_gestion']