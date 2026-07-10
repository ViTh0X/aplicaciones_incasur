from django.urls import path
from . import views

urlpatterns = [
    path('comisiones-gastos',views.comisiones_gastos,name='comisiones_gastos'),
    path('reporte-rr3',views.reporte_rr3,name='reporte_rr3'),
]