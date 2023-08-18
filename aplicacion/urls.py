from django.urls import path, include
from .views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', index, name="inicio"),

    path('moto/', Moto, name="moto"),
    path('taller/', Taller, name="taller"),

    path('moto_form/', motoForm, name="moto_form"),
    path('moto_form2/', motoForm2, name="moto_form2"),

    path('buscar_modelo/', buscarModelo, name="buscar_modelo"),
    path('buscar2/', buscar2, name="buscar2"),

    path('accesorio/', accesorios, name="accesorio"),
    path('update_accesorio/<id_accesorio>/', updateAccesorio, name="update_accesorio"),
    path('delete_accesorio/<id_accesorio>/', deleteAccesorio, name="delete_accesorio"),
    path('create_accesorio/', createAccesorio, name="create_accesorio"),

    path('cliente/', ClienteList.as_view(), name="cliente"),
    path('create_cliente/', ClienteCreate.as_view(), name="create_cliente"),
    path('detail_cliente/<int:pk>/', ClienteDetail.as_view(), name="detail_cliente"),
    path('update_cliente/<int:pk>/', ClienteUpdate.as_view(), name="update_cliente"),
    path('delete_cliente/<int:pk>/', ClienteDelete.as_view(), name="delete_cliente"),

    path('login/', login_request, name="login"),
    path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html"), name="logout"),
    path('register/', register, name="register"),

    path('editar_perfil/', editarPerfil, name="editar_perfil"),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),
]
