# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('idalumno', models.CharField(max_length=10)),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('edad', models.CharField(max_length=2)),
                ('sexo', models.CharField(max_length=1)),
                ('fnacimiento', models.CharField(max_length=8)),
                ('telefono', models.CharField(max_length=8)),
                ('padre', models.CharField(max_length=100)),
                ('madre', models.CharField(max_length=100)),
                ('encargado', models.CharField(max_length=100)),
                ('parentesco', models.CharField(max_length=1)),
                ('direccion', models.CharField(max_length=500)),
                ('estado', models.CharField(max_length=1)),
                ('idgrado', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'alumno',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ano',
            fields=[
                ('idano', models.IntegerField(serialize=False, primary_key=True)),
                ('ano', models.IntegerField()),
                ('observacion', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'ano',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Asignaturasbasica',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('idasignatura', models.CharField(max_length=10)),
                ('asignatura', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'asignaturasbasica',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Asinaturas',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('idasignatura', models.CharField(max_length=10)),
                ('asignatura', models.CharField(max_length=50)),
                ('idgrado', models.CharField(max_length=10)),
                ('idmae', models.CharField(max_length=9)),
                ('estado', models.IntegerField()),
            ],
            options={
                'db_table': 'asinaturas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cargamaestro',
            fields=[
                ('idtabla', models.IntegerField(serialize=False, primary_key=True)),
                ('idame', models.CharField(max_length=10)),
                ('idano', models.IntegerField()),
            ],
            options={
                'db_table': 'cargamaestro',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cargasignaturabasica',
            fields=[
                ('idtabla', models.IntegerField(serialize=False, primary_key=True)),
                ('idasigntura', models.CharField(max_length=10)),
                ('idmae', models.CharField(max_length=10)),
                ('idano', models.IntegerField()),
            ],
            options={
                'db_table': 'cargasignaturabasica',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cargasignaturamedia',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('idasigntura', models.CharField(max_length=10)),
                ('idmae', models.CharField(max_length=10)),
                ('idano', models.IntegerField()),
                ('estado', models.IntegerField()),
            ],
            options={
                'db_table': 'cargasignaturamedia',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Evaluacion',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('idmae', models.CharField(max_length=9)),
                ('iditem', models.IntegerField()),
                ('idgrado', models.CharField(max_length=11)),
                ('resultado', models.IntegerField()),
                ('idano', models.IntegerField()),
            ],
            options={
                'db_table': 'evaluacion',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Grados',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('idgrado', models.CharField(max_length=11)),
                ('idmae', models.CharField(max_length=9)),
                ('nivel', models.CharField(max_length=10)),
                ('grado', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'grados',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('iditem', models.IntegerField()),
                ('item', models.IntegerField()),
            ],
            options={
                'db_table': 'items',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Maestros',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('idmae', models.CharField(max_length=9)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('edad', models.CharField(max_length=2)),
                ('sexo', models.CharField(max_length=1)),
                ('aingreso', models.CharField(max_length=4)),
                ('estudio', models.CharField(max_length=75)),
                ('telefono', models.CharField(max_length=8)),
                ('direccion', models.CharField(max_length=200)),
                ('estado', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'maestros',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('idalumno', models.CharField(max_length=10)),
                ('idgrado', models.CharField(max_length=11)),
                ('estado', models.CharField(max_length=2)),
                ('idusuario', models.CharField(max_length=9)),
                ('idano', models.CharField(max_length=11)),
            ],
            options={
                'db_table': 'matricula',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mes',
            fields=[
                ('id', models.IntegerField(unique=True, serialize=False, primary_key=True)),
                ('idmes', models.IntegerField()),
                ('mes', models.CharField(max_length=12)),
                ('estado', models.IntegerField()),
            ],
            options={
                'db_table': 'mes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Notabasica',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('idalumno', models.CharField(max_length=10)),
                ('idmae', models.CharField(max_length=10)),
                ('idgrado', models.CharField(max_length=10)),
                ('idasignatura', models.CharField(max_length=10)),
                ('periodo', models.CharField(max_length=2)),
                ('a1m1', models.IntegerField()),
                ('a2m1', models.IntegerField()),
                ('a3m1', models.IntegerField()),
                ('a4m1', models.IntegerField()),
                ('proa1', models.FloatField()),
                ('p601', models.FloatField()),
                ('exam1', models.IntegerField()),
                ('p401', models.FloatField()),
                ('nmes1', models.FloatField()),
                ('a1m2', models.IntegerField()),
                ('a2m2', models.IntegerField()),
                ('a3m2', models.IntegerField()),
                ('a4m2', models.IntegerField()),
                ('proa2', models.FloatField()),
                ('p602', models.FloatField()),
                ('exam2', models.IntegerField()),
                ('p402', models.FloatField()),
                ('nmes2', models.FloatField()),
                ('a1m3', models.IntegerField()),
                ('a2m3', models.IntegerField()),
                ('a3m3', models.IntegerField()),
                ('a4m3', models.IntegerField()),
                ('proa3', models.FloatField()),
                ('p603', models.FloatField()),
                ('exam3', models.IntegerField()),
                ('p403', models.FloatField()),
                ('nmes3', models.FloatField()),
                ('promtrim', models.FloatField()),
                ('idano', models.IntegerField()),
            ],
            options={
                'db_table': 'notabasica',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Notamensualbasica',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('idalumno', models.CharField(max_length=10)),
                ('idmae', models.CharField(max_length=10)),
                ('idgrado', models.CharField(max_length=10)),
                ('idasignatura', models.CharField(max_length=10)),
                ('idmes', models.IntegerField()),
                ('periodo', models.CharField(max_length=2)),
                ('a1', models.IntegerField()),
                ('a2', models.IntegerField()),
                ('a3', models.IntegerField()),
                ('a4', models.IntegerField()),
                ('promedio', models.FloatField()),
                ('p60', models.FloatField()),
                ('examen', models.IntegerField()),
                ('p40', models.FloatField()),
                ('promes', models.FloatField()),
                ('idano', models.IntegerField()),
            ],
            options={
                'db_table': 'notamensualbasica',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Notas',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('idalumno', models.CharField(max_length=10)),
                ('idasignatura', models.CharField(max_length=10)),
                ('idmae', models.CharField(max_length=10)),
                ('idgrado', models.CharField(max_length=10)),
                ('periodo', models.CharField(max_length=10)),
                ('a1', models.IntegerField(db_column='A1')),
                ('a2', models.IntegerField(db_column='A2')),
                ('a3', models.IntegerField(db_column='A3')),
                ('a4', models.IntegerField(db_column='A4')),
                ('a5', models.IntegerField(db_column='A5')),
                ('p50', models.FloatField(db_column='P50')),
                ('examen', models.IntegerField(db_column='EXAMEN')),
                ('p20', models.FloatField(db_column='P20')),
                ('examenp', models.IntegerField(db_column='EXAMENP')),
                ('p30', models.FloatField(db_column='P30')),
                ('pf', models.FloatField(db_column='PF')),
                ('ano', models.CharField(max_length=11)),
                ('recup', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'notas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idusuario', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('usuario', models.CharField(max_length=10)),
                ('idmae', models.CharField(max_length=9)),
                ('idgrado', models.IntegerField()),
            ],
            options={
                'db_table': 'usuario',
            },
            bases=(models.Model,),
        ),
    ]
