from django.contrib import admin
from .models import Task
# Register your models here.

class Info(admin.ModelAdmin):
    readonly_fields = ("created",) ## Clase que crea tuplas para mostrar en la interfaz de usuario los campos aqui pasados

admin.site.register(Task, Info) ##Muestra la tabla en la pagina del admin
