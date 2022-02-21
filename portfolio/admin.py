from django.contrib import admin
from .models import Project

# Clase para extender las funcionalidades de la pagina admin
class ProjectAdmin(admin.ModelAdmin):
    # Mostrar campos de solo lectura en el panel de administrador
    readonly_fields = ('fechaCreacion', 'fechaActualizacion')

# Registrar Modelo Project, el segundo parametro es la configuracion extendida (ProjectAdmin)
admin.site.register(Project, ProjectAdmin)