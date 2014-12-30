# This ims an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Alumno(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    idalumno = models.CharField(max_length=10)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    edad = models.CharField(max_length=2)
    sexo = models.CharField(max_length=1)
    fnacimiento = models.CharField(max_length=8)
    telefono = models.CharField(max_length=8)
    padre = models.CharField(max_length=100)
    madre = models.CharField(max_length=100)
    encargado = models.CharField(max_length=100)
    parentesco = models.CharField(max_length=1)
    direccion = models.CharField(max_length=500)
    estado = models.CharField(max_length=1)
    idgrado = models.CharField(max_length=10)

    class Meta:
        
        db_table = 'alumno'


class Ano(models.Model):
    idano = models.IntegerField(primary_key=True)
    ano = models.IntegerField()
    observacion = models.CharField(max_length=25)

    class Meta:
        
        db_table = 'ano'


class Asignaturasbasica(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    idasignatura = models.CharField(max_length=10)
    asignatura = models.CharField(max_length=25)

    class Meta:
        
        db_table = 'asignaturasbasica'


class Asinaturas(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    idasignatura = models.CharField(max_length=10)
    asignatura = models.CharField(max_length=50)
    idgrado = models.CharField(max_length=10)
    idmae = models.CharField(max_length=9)
    estado = models.IntegerField()

    class Meta:
        
        db_table = 'asinaturas'


class Cargamaestro(models.Model):
    idtabla = models.IntegerField(primary_key=True)
    idame = models.CharField(max_length=10)
    idano = models.IntegerField()

    class Meta:
        
        db_table = 'cargamaestro'


class Cargasignaturabasica(models.Model):
    idtabla = models.IntegerField(primary_key=True)
    idasigntura = models.CharField(max_length=10)
    idmae = models.CharField(max_length=10)
    idano = models.IntegerField()

    class Meta:
        
        db_table = 'cargasignaturabasica'


class Cargasignaturamedia(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    idasigntura = models.CharField(max_length=10)
    idmae = models.CharField(max_length=10)
    idano = models.IntegerField()
    estado = models.IntegerField()

    class Meta:
        
        db_table = 'cargasignaturamedia'


class Evaluacion(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    idmae = models.CharField(max_length=9)
    iditem = models.IntegerField()
    idgrado = models.CharField(max_length=11)
    resultado = models.IntegerField()
    idano = models.IntegerField()

    class Meta:
        
        db_table = 'evaluacion'


class Grados(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    idgrado = models.CharField(max_length=11)
    idmae = models.CharField(max_length=9)
    nivel = models.CharField(max_length=10)
    grado = models.CharField(max_length=50)
    estado = models.CharField(max_length=1)

    class Meta:
        
        db_table = 'grados'


class Items(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    iditem = models.IntegerField()
    item = models.IntegerField()

    class Meta:
        
        db_table = 'items'


class Maestros(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    idmae = models.CharField(max_length=9)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.CharField(max_length=2)
    sexo = models.CharField(max_length=1)
    aingreso = models.CharField(max_length=4)
    estudio = models.CharField(max_length=75)
    telefono = models.CharField(max_length=8)
    direccion = models.CharField(max_length=200)
    estado = models.CharField(max_length=1)

    class Meta:
        
        db_table = 'maestros'


class Matricula(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    idalumno = models.CharField(max_length=10)
    idgrado = models.CharField(max_length=11)
    estado = models.CharField(max_length=2)
    idusuario = models.CharField(max_length=9)
    idano = models.CharField(max_length=11)

    class Meta:
        
        db_table = 'matricula'


class Mes(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    idmes = models.IntegerField()
    mes = models.CharField(max_length=12)
    estado = models.IntegerField()

    class Meta:
        
        db_table = 'mes'


class Notabasica(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    idalumno = models.CharField(max_length=10)
    idmae = models.CharField(max_length=10)
    idgrado = models.CharField(max_length=10)
    idasignatura = models.CharField(max_length=10)
    periodo = models.CharField(max_length=2)
    a1m1 = models.IntegerField()
    a2m1 = models.IntegerField()
    a3m1 = models.IntegerField()
    a4m1 = models.IntegerField()
    proa1 = models.FloatField()
    p601 = models.FloatField()
    exam1 = models.IntegerField()
    p401 = models.FloatField()
    nmes1 = models.FloatField()
    a1m2 = models.IntegerField()
    a2m2 = models.IntegerField()
    a3m2 = models.IntegerField()
    a4m2 = models.IntegerField()
    proa2 = models.FloatField()
    p602 = models.FloatField()
    exam2 = models.IntegerField()
    p402 = models.FloatField()
    nmes2 = models.FloatField()
    a1m3 = models.IntegerField()
    a2m3 = models.IntegerField()
    a3m3 = models.IntegerField()
    a4m3 = models.IntegerField()
    proa3 = models.FloatField()
    p603 = models.FloatField()
    exam3 = models.IntegerField()
    p403 = models.FloatField()
    nmes3 = models.FloatField()
    promtrim = models.FloatField()
    idano = models.IntegerField()

    class Meta:
        
        db_table = 'notabasica'


class Notamensualbasica(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    idalumno = models.CharField(max_length=10)
    idmae = models.CharField(max_length=10)
    idgrado = models.CharField(max_length=10)
    idasignatura = models.CharField(max_length=10)
    idmes = models.IntegerField()
    periodo = models.CharField(max_length=2)
    a1 = models.IntegerField()
    a2 = models.IntegerField()
    a3 = models.IntegerField()
    a4 = models.IntegerField()
    promedio = models.FloatField()
    p60 = models.FloatField()
    examen = models.IntegerField()
    p40 = models.FloatField()
    promes = models.FloatField()
    idano = models.IntegerField()

    class Meta:
        
        db_table = 'notamensualbasica'


class Notas(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    idalumno = models.CharField(max_length=10)
    idasignatura = models.CharField(max_length=10)
    idmae = models.CharField(max_length=10)
    idgrado = models.CharField(max_length=10)
    periodo = models.CharField(max_length=10)
    a1 = models.IntegerField(db_column='A1')  # Field name made lowercase.
    a2 = models.IntegerField(db_column='A2')  # Field name made lowercase.
    a3 = models.IntegerField(db_column='A3')  # Field name made lowercase.
    a4 = models.IntegerField(db_column='A4')  # Field name made lowercase.
    a5 = models.IntegerField(db_column='A5')  # Field name made lowercase.
    p50 = models.FloatField(db_column='P50')  # Field name made lowercase.
    examen = models.IntegerField(db_column='EXAMEN')  # Field name made lowercase.
    p20 = models.FloatField(db_column='P20')  # Field name made lowercase.
    examenp = models.IntegerField(db_column='EXAMENP')  # Field name made lowercase.
    p30 = models.FloatField(db_column='P30')  # Field name made lowercase.
    pf = models.FloatField(db_column='PF')  # Field name made lowercase.
    ano = models.CharField(max_length=11)
    recup = models.IntegerField(blank=True, null=True)

    class Meta:
        
        db_table = 'notas'


class Usuario(models.Model):
    idusuario = models.CharField(primary_key=True, max_length=10)
    usuario = models.CharField(max_length=10)
    idmae = models.CharField(max_length=9)
    idgrado = models.IntegerField()

    class Meta:
        
        db_table = 'usuario'
