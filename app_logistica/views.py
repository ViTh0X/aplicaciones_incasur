from django.shortcuts import render, redirect, get_object_or_404

#Login
from .forms import  Login_Formulario,AlmacenesForm,ItemsForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Items,Almacenes,HistorialInventarios
from django.db.models import Count,Exists

from datetime import datetime

from utilidades.genera_qr import generar_qr

# Create your views here.
@login_required(login_url="login_logistica")
def logistica_items(request):
    items =  Items.objects.all()
    return render(request,'logistica/items.html',{'items':items})

@login_required(login_url="login_logistica")
def agregar_items(request):
    if request.method == 'POST':
        form = ItemsForm(request.POST)
        if form.is_valid():
            item = form.save()
            qr_link = f"http://192.168.1.8/aplicaciones-incasur/logistica/editar-item-celular/{item.pk}"
            nombre_archivo_qr = generar_qr(item.pk,qr_link)
            item.imagen_qr.name = f"imagenes_qr/{nombre_archivo_qr}"
            item.save()
            return redirect ('logistica_items')        
    else:
        form = ItemsForm()
    return render(request,'logistica/formulario_agregar_items.html',{'form':form})

@login_required(login_url="login_logistica")
def editar_item_celular(request,pk):            
    item = get_object_or_404(Items,pk=pk)
    año = datetime.now().year
    inventario = HistorialInventarios.objects.filter(id_item=pk,fecha_modificacion__year=año)    
    #inventario = get_object_or_404(HistorialInventarios,id_item=pk,fecha_modificacion__year=año)
    if request.method == 'POST':
        form = ItemsForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
        return redirect('logistica_items')
    else:
        form = ItemsForm(instance=item)
    return render(request,'logistica/formulario_editar_item_celular.html',{'form':form,'item':item,'inventario':inventario})


@login_required(login_url="login_logistica")
def editar_item(request,pk):        
    item = get_object_or_404(Items,pk=pk)
    if request.method == 'POST':
        form = ItemsForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
        return redirect('logistica_items')
    else:
        form = ItemsForm(instance=item)
    return render(request,'logistica/formulario_editar_item.html',{'form':form,'item':item})
    
@login_required(login_url="login_logistica")
def logistica_almacenes(request):
    almacenes = Almacenes.objects.annotate(total_articulos=Count('items'))         
    return render(request,'logistica/almacenes.html',{'almacenes':almacenes})

@login_required(login_url="login_logistica")
def agregar_almacenes(request):
    if request.method == "POST":
        form = AlmacenesForm(request.POST)        
        if form.is_valid():
            form.save()
            return redirect('logistica_almacenes')                    
    else:
        form = AlmacenesForm()
    return render(request,'logistica/formulario_agregar_almacenes.html',{'form':form})

@login_required(login_url="login_logistica")
def editar_almacen(request,pk):
    almacen = get_object_or_404(Almacenes,pk=pk)
    if request.method == 'POST':
        form = AlmacenesForm(request.POST, instance=almacen)
        if form.is_valid():
            form.save()
        return redirect('logistica_almacenes')
    else:
        form = AlmacenesForm(instance=almacen)                
    return render(request,'logistica/formulario_editar_almacen.html',{'form':form})

@login_required(login_url="login_logistica")
def eliminar_almacen(request,pk):
    almacen = get_object_or_404(Almacenes,pk=pk)
    if request.method == 'POST':
        almacen.delete()
        return redirect('logistica_almacenes')        
    return render(request,'logistica/confirmar_eliminar_almacen.html',{'almacen':almacen})
        
@login_required(login_url="login_logistica")        
def items_por_almacen(request,pk):
    año = datetime.now().year
    inventario_anio_actual = HistorialInventarios.objects.filter(id_item=pk,fecha_modificacion__year=año)
        
    items = Items.objects.filter(id_almacen = pk).annotate(inventario_anio_actual=Exists(inventario_anio_actual))
    return render(request,'logistica/items.html',{'items':items})

@login_required(login_url="login_logistica")
def logistica_movimientos(request):
    return render(request,'logistica/movimientos.html')


@login_required(login_url="login_logistica")
def logistica_historial_inventario(request):
    return render(request,'logistica/historial_inventario.html')

@login_required(login_url="login_logistica")
def logistica_colaboradores(request):
    return render(request,'logistica/colaboradores.html')


    


def login_logistica(request):
    if request.user.is_authenticated:
        next_url = request.GET.get('next')
        if next_url:
            return redirect(next_url)
        return redirect('logistica_items')
    else:
        if request.method == 'POST':
            form = Login_Formulario(request.POST or None)
            if form.is_valid():
                data = form.cleaned_data
                usuario = data['usuario']
                contraseña = data['password']
                user = authenticate(request,username=usuario,password=contraseña)
                if user is not None:
                    login(request,user)
                    next_url = request.POST.get('next') or request.GET.get('next')
                    if next_url:
                        return redirect(next_url)
                    else:
                        return redirect('logistica_items')        
                else:
                    messages.warning(request,"Usuario o Contraseña Incorrectos")
        else:
            form =  Login_Formulario()
        return render(request,'logistica/login.html',{'form':form})

@login_required(login_url="login_logistica")
def logout_logistica(request):
    logout(request)
    return redirect('login_logistica')