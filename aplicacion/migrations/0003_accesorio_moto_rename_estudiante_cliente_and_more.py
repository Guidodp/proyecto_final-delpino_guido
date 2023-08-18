# Generated by Django 4.2.3 on 2023-08-18 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0002_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accesorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=50)),
                ('origen', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Moto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.IntegerField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Estudiante',
            new_name='Cliente',
        ),
        migrations.RenameModel(
            old_name='Entregable',
            new_name='Taller',
        ),
        migrations.DeleteModel(
            name='Curso',
        ),
        migrations.DeleteModel(
            name='Profesor',
        ),
        migrations.RenameField(
            model_name='taller',
            old_name='nombre',
            new_name='mecanico',
        ),
    ]
