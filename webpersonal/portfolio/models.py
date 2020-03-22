from django.db import models

# Create your models here.

#Crear mis modelos
class project(models.Model): #siempre en singular y con mayusculas
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="imagen", upload_to="projects")
    link = models.URLField(null=True, blank=True, verbose_name="Enlace")
    created = models.DateField(auto_now_add=True,verbose_name="Fecha de creación")
    updated = models.DateField(auto_now=True,verbose_name="Fecha de edición")
    


    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural =  "Proyectos"
        ordering = ["-created"]

    def __str__(self):
        return self.title