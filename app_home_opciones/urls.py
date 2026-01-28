from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_opciones,name='home_opciones'),
]
