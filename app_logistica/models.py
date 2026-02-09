from django.db import models
from django.conf import settings
import os

# Create your models here.
class Colaboradores(models.Model):
    codigo_colaborador = models.AutoField(primary_key=True)
    nombre_colaborador = models.CharField(max_length=150)
    usuario_sistema = models.CharField(max_length=25)
    correo = models.CharField(max_length=50)
    usuario_sentinel = models.CharField(max_length=15)
    usuario_sbs = models.CharField(max_length=15)
    usuario_windows = models.CharField(max_length=15)
    usuario_reloj_control = models.CharField(max_length=15)
    codigo_impresion_colaborador = models.CharField(max_length=20)
    cargo_colaborador = models.ForeignKey('CargoColaboradores', models.DO_NOTHING)
    fecha_modificacion = models.DateTimeField()
    estado_colaboradores = models.ForeignKey('EstadoColaboradores', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'colaboradores'            


class CargoColaboradores(models.Model):
    codigo_cargo = models.AutoField(primary_key=True)
    nombre_cargo = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'cargo_colaboradores'


class EstadoColaboradores(models.Model):
    codigo_estado = models.AutoField(primary_key=True)
    nombre_estado = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'estado_colaboradores'      
        
        
class AreasEmpresa(models.Model):
    id_area = models.AutoField(primary_key=True)
    nombre_area = models.CharField(max_length=40)
    descripcion_area = models.CharField(max_length=150)
    fecha_modificacion = models.DateTimeField(auto_now=True)
        
    class Meta:
        db_table = 'areas_empresa'
        
    def __str__(self):
        return self.nombre_area
    
    
class Almacenes(models.Model):
    id_almacen = models.AutoField(primary_key=True)
    nombre_almacen = models.CharField(max_length=60)
    descripcion_almacen = models.CharField(max_length=150)
    direccion_almacen = models.CharField(max_length=120)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'almacences'
    
    def __str__(self):
        return self.nombre_almacen
    

class TipoEstadoItems(models.Model):
    id_estado = models.AutoField(primary_key=True)
    nombre_estado = models.CharField(max_length=60)
    descripcion_estado = models.CharField(max_length=150)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'tipo_estado_items'
        
    def __str__(self):
        return self.nombre_estado
    

class Items(models.Model):
    id_item = models.AutoField(primary_key=True)
    nombre_item = models.CharField(max_length=100)
    descripcion_item = models.CharField(max_length=200,blank=True,null=True)
    imagen_qr = models.ImageField(upload_to='imagenes_qr/',blank=True,null=True)
    id_area = models.ForeignKey(AreasEmpresa,on_delete=models.CASCADE,null=True,blank=True)
    id_estado = models.ForeignKey(TipoEstadoItems,on_delete=models.CASCADE)
    id_almacen = models.ForeignKey(Almacenes,on_delete=models.CASCADE,null=True,blank=True)
    id_usuario = models.ForeignKey(Colaboradores,on_delete=models.CASCADE,null=True,blank=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'items'
    
    def __str__(self):
        return self.nombre_item
    
    
class HistorialInventarios(models.Model):
    id_historial = models.AutoField(primary_key=True)
    id_item = models.ForeignKey(Items,on_delete=models.CASCADE)
    nombre_area = models.CharField(max_length=40)
    nombre_almacen = models.CharField(max_length=60)
    nombre_usuario = models.CharField(max_length=150)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'historial_inventarios'
        
    def __str__(self):
        return self.id_historial
    
    
class ItemsEliminados(models.Model):
    id_eliminados = models.AutoField(primary_key=True)
    id_item = models.ForeignKey(Items,on_delete=models.CASCADE)
    nombre_area = models.CharField(max_length=40)
    nombre_almacen = models.CharField(max_length=60)
    nombre_usuario = models.CharField(max_length=150)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'items_eliminados'
        
    def __str__(self):
        return self.id_historial
    
    
class ItemsMovimientos(models.Model):
    id_movimiento = models.AutoField(primary_key=True)
    nombre_origen = models.CharField(max_length=150)
    nombre_destino = models.CharField(max_length=150)
    id_item = models.ForeignKey(Items,on_delete=models.CASCADE)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'items_movimientos'
        
    def __str__(self):
        return self.id_movimiento
    
    
        