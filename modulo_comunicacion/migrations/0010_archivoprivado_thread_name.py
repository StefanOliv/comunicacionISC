# Generated by Django 4.1.5 on 2023-02-27 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_comunicacion', '0009_archivopublico_remove_archivoprivado_filegroup_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='archivoprivado',
            name='thread_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]