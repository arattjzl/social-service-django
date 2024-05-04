# Generated by Django 5.0.1 on 2024-04-16 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instituciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripción')),
                ('direccion', models.CharField(max_length=250, verbose_name='Dirección')),
                ('telefono', models.CharField(max_length=10)),
                ('mail', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='fotos', verbose_name='Imagen')),
            ],
        ),
    ]
