from django.contrib import admin

# Register your models here.
from .models import Curso, Estudiante, Direccion, Profesor

admin.site.register(Curso)
admin.site.register(Profesor)
admin.site.register(Estudiante)
admin.site.register(Direccion)