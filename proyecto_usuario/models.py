from django.db import models
from django.contrib.auth.models import User

class registro_proyecto(models.Model):
    idproyecto = models.AutoField(primary_key=True, db_index=True, editable=False)
    nombreproyecto = models.CharField( blank = True, max_length = 50, null = False)
    descripcionProyecto = models.CharField(max_length= 80, null = True)
    fechaincio = models.DateTimeField(auto_now_add=True)
    fk_user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
            db_table = 'Proyecto'
            verbose_name = 'Proyecto'
            verbose_name_plural = 'Proyectos'

    def __str__(self):
        return  self.nombreproyecto

class conexionuser_proyec(models.Model):
    fk_proyecto = models.ForeignKey(registro_proyecto, on_delete=models.CASCADE)
    fk_user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Conexion'
        verbose_name = 'conexion'
        verbose_name_plural = 'conexiones'
