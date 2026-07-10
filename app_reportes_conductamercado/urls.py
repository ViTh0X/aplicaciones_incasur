from django.urls import path
from . import views

urlpatterns = [
    path('comisiones-gastos',views.comisiones_gastos,name='comisiones_gastos'),
]