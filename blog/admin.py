from django.contrib import admin
from .models import Usuario, Mamadas

@admin.register(Usuario)

class adminUsuario(admin.ModelAdmin):
	list_display = ('nombre','email','contra')


@admin.register(Mamadas)

class adminMamadas(admin.ModelAdmin):
	list_display = ('user','telefono','direccion')