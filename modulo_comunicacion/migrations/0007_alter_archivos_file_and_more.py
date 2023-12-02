# Generated by Django 4.1.5 on 2023-02-27 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_comunicacion', '0006_mensajeprivados_archivopriv_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archivos',
            name='file',
            field=models.FileField(upload_to='archivos/canales'),
        ),
        migrations.AlterField(
            model_name='mensajeprivados',
            name='archivopriv',
            field=models.FileField(null=True, upload_to='media/'),
        ),
    ]