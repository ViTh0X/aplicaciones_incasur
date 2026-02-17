from django.urls import path
from . import views


urlpatterns = [
    path('',views.logistica_items,name='logistica_items'),
    path('agregar-items',views.agregar_items,name='agregar_items'),
    path('editar-item/<int:pk>/',views.editar_item,name='editar_item'),
    path('editar-item-celular/<int:pk>/',views.editar_item_celular,name='editar_item_celular'),
    path('inventariar-articulo/<int:pk>/',views.inventariar_articulo,name='inventariar_articulo'),
    path('eliminar-articulo/<int:pk>/',views.eliminar_articulo,name='eliminar_articulo'),
    path('historial-inventario-articulo/<int:pk>/',views.historial_inventario_articulo,name='historial_inventario_articulo'),
    path('movimientos-articulo/<int:pk>/',views.movimientos_articulo,name='movimientos_articulo'),
    #path('',views.logistica_almacenes,name='logistica_items'),
    path('almacenes',views.logistica_almacenes,name='logistica_almacenes'),
    path('agregar-almacenes',views.agregar_almacenes,name='agregar_almacenes'),
    path('editar-almacen/<int:pk>/',views.editar_almacen,name='editar_almacen'),
    path('eliminar-almacen/<int:pk>/',views.eliminar_almacen,name='eliminar_almacen'),
    path('items-por-almace/<int:pk>/',views.items_por_almacen,name='items_por_almacen'),
    path('movimientos',views.logistica_movimientos,name='logistica_movimientos'),
    path('historial-inventario',views.logistica_historial_inventario,name='logistica_historial_inventario'),
    path('colaboradores',views.logistica_colaboradores,name='logistica_colaboradores'),    
    path('login',views.login_logistica,name='login_logistica'),
    path('logout',views.logout_logistica,name='logout_logistica'),    
]
