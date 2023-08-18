from django.contrib import admin
from .models import Moto, Accesorio, Cliente, Taller, Avatar

# Register your models here.
admin.site.register(Moto)
admin.site.register(Accesorio)
admin.site.register(Cliente)
admin.site.register(Taller)
admin.site.register(Avatar)