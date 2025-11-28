from django.contrib import admin
from .models import Usuario, Endereco


admin.site.register(Endereco) 
admin.site.register(Usuario)