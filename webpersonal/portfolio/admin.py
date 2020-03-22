from django.contrib import admin
from .models import project #importando el modelo de la base de datos
# Register your models here.
#registrando el modelos
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ("created","updated")

admin.site.register(project, ProjectAdmin)
