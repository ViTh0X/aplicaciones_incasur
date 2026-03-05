from django.urls import path
from . import views

urlpatterns = [
    path('',views.main_seguimiento_actividades,name='main_seguimiento_actividades'),
    path('lista-tareas/<int:pk>',views.ver_tareas,name='ver_tareas'),
    path('agregar-proyecto',views.agregar_proyecto,name='agregar_proyecto'),
    path('agregar-tarea/<int:pk>',views.agregar_tarea,name='agregar_tarea'),
    path('agregar-subtarea/<int:pk>',views.agregar_subtarea,name='agregar_subtarea'),
    path('agregar-subtarea-seleccionada/<int:pk>',views.agregar_subtarea_seleccionada,name='agregar_subtarea_seleccionada'),
    path('editar-subtarea/<int:pk>',views.editar_subtarea,name='editar_subtarea'),
    path('agregar-gestion/<int:pk>',views.agregar_gestion,name='agregar_gestion'),
    path('lista-gestion/<int:pk>',views.listar_gestion,name='listar_gestion'),
    path('imprimir-gestion<int:pk>',views.imprimir_gestion,name='imprimir_gestion')
]