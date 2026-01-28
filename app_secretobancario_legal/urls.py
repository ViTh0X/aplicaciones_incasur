from django.urls import path
from . import views

urlpatterns = [
    path('',views.generar_word_secban,name='generar_word_secban'),
]
