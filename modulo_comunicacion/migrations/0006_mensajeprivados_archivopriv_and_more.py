# Generated by Django 4.1.5 on 2023-02-21 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_comunicacion', '0005_mensajeprivados'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensajeprivados',
            name='archivopriv',
            field=models.FileField(null=True, upload_to='modelo_comunicacion/archivos/privados'),
        ),
        migrations.AlterField(
            model_name='mensajeprivados',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
