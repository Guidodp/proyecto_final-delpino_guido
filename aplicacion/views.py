from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import *
from .forms import *

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DetailView
from django.views.generic import DeleteView

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "aplicacion/base.html")



def clientes(request):
    return render(request, "aplicacion/clientes.html")

def accesorios(request):
    return render(request, "aplicacion/accesorios.html")

@login_required
def motos(request):
    ctx = {"motos": motos.objects.all() }
    return render(request, "aplicacion/motos.html", ctx)

@login_required
def motoForm(request):
    if request.method == "POST":                
        moto = Moto(marca=request.POST['marca'], modelo=request.POST['modelo'])
        moto.save()
        return HttpResponse("Se grabo con exito la moto!")
    
    return render(request, "aplicacion/motoForm.html")

@login_required
def motoForm2(request):
    if request.method == "POST":   
        miForm = MotoForm(request.POST)
        if miForm.is_valid():
            moto_marca = miForm.cleaned_data.get('marca')
            moto_modelo = miForm.cleaned_data.get('modelo')
            moto = moto(marca=moto_modelo, modelo=moto_modelo)
            moto.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm = MotoForm()

    return render(request, "aplicacion/motoForm2.html", {"form":miForm})

@login_required
def buscarModelo(request):
    return render(request, "aplicacion/buscarModelo.html")

@login_required
def buscar2(request):
    if request.GET['modelo']:
        modelo = request.GET['modelo']
        motos = Moto.objects.filter(modelo__icontains=modelo)
        return render(request, 
                      "aplicacion/resultadosModelo.html", 
                      {"modelo": modelo, "motos":motos})
    return HttpResponse("No se ingresaron datos para buscar!")


#__________________________________
@login_required
def Accesorio(request):
     ctx = {'accesorio': Accesorio.objects.all() }
     return render(request, "aplicacion/accesorios.html", ctx)

@login_required
def updateAccesorio(request, id_accesorio):
    accesorio = Accesorio.objects.get(id=id_accesorio)
    if request.method == "POST":
        miForm = AccesorioForm(request.POST)
        if miForm.is_valid():
            accesorio.nombre = miForm.cleaned_data.get('nombre')
            accesorio.marca = miForm.cleaned_data.get('marca')
            accesorio.origen = miForm.cleaned_data.get('origen')
            accesorio.save()
            return redirect(reverse_lazy('accesorios'))   
    else:
        miForm = AccesorioForm(initial={'nombre':accesorio.nombre, 
                                       'marca':accesorio.marca, 
                                       'origen':accesorio.origen, 
                                       'accesorio':accesorio.accesorio})         
    return render(request, "aplicacion/accesorioForm.html", {'form': miForm})   

@login_required
def deleteAccesorio(request, id_accesorio):
    accesorio = Accesorio.objects.get(id=id_accesorio)
    accesorio.delete()
    return redirect(reverse_lazy('accesorios'))

@login_required
def createAccesorio(request):    
    if request.method == "POST":
        miForm = AccesorioForm(request.POST)
        if miForm.is_valid():
            p_nombre = miForm.cleaned_data.get('nombre')
            p_marca= miForm.cleaned_data.get('marca')
            p_modelo = miForm.cleaned_data.get('modelo')
            p_origen = miForm.cleaned_data.get('origen')
            accesorio = Accesorio(nombre=p_nombre, 
                             marca=p_marca,
                             modelo=p_modelo,
                             origen=p_origen,
                             )
            accesorio.save()
            return redirect(reverse_lazy('accesorios'))
    else:
        miForm = AccesorioForm()

    return render(request, "aplicacion/AccesorioForm.html", {"form":miForm})

#______ Class Based View

class ClienteList(LoginRequiredMixin, ListView):
    model = Cliente

class ClienteCreate(LoginRequiredMixin, CreateView):
    model = Cliente
    fields = ['nombre', 'apellido', 'email']
    success_url = reverse_lazy('clientes')

class ClienteDetail(LoginRequiredMixin, DetailView):
    model = Cliente

class ClienteUpdate(LoginRequiredMixin, UpdateView):
    model = Cliente
    fields = ['nombre', 'apellido', 'email']
    success_url = reverse_lazy('clientes')    

class ClienteDelete(LoginRequiredMixin, DeleteView):
    model = Cliente
    success_url = reverse_lazy('clientes')    

#____________ Login, Logout, Registracion
# 

def login_request(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            clave = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=clave)
            if user is not None:
                login(request, user)
    #_____________________                
                try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar = '/media/avatares/default.png'
                finally:
                    request.session['avatar'] = avatar

                return render(request, "aplicacion/base.html", {"mensaje": f"Bienvenido {usuario}"})
            else:
                return render(request, "aplicacion/login.html", {"form":miForm, "mensaje": "Datos Inválidos"})
        else:    
            return render(request, "aplicacion/login.html", {"form":miForm, "mensaje": "Datos Inválidos"})

    miForm = AuthenticationForm()

    return render(request, "aplicacion/login.html", {"form":miForm})    

def register(request):
    if request.method == 'POST':
        form = RegistroUsuariosForm(request.POST) # UserCreationForm 
        if form.is_valid():  # Si pasó la validación de Django
            usuario = form.cleaned_data.get('username')
            form.save()
            return render(request, "aplicacion/base.html", {"mensaje":"Usuario Creado"})        
    else:
        form = RegistroUsuariosForm() # UserCreationForm 

    return render(request, "aplicacion/registro.html", {"form": form})   

#_________________ Registración de usuarios
# 

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            usuario.email = form.cleaned_data.get('email')
            usuario.password1 = form.cleaned_data.get('password1')
            usuario.password2 = form.cleaned_data.get('password2')
            usuario.first_name = form.cleaned_data.get('first_name')
            usuario.last_name = form.cleaned_data.get('last_name')
            usuario.save()
            return render(request, "aplicacion/base.html", {'mensaje': f"Usuario {usuario.username} actualizado correctamente"})
        else:
            return render(request, "aplicacion/editarPerfil.html", {'form': form})
    else:
        form = UserEditForm(instance=usuario)
    return render(request, "aplicacion/editarPerfil.html", {'form': form, 'usuario':usuario.username})

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES)
        if form.is_valid():
            u = User.objects.get(username=request.user)
            #_________________ Esto es para borrar el avatar anterior
            avatarViejo = Avatar.objects.filter(user=u)
            if len(avatarViejo) > 0: # Si esto es verdad quiere decir que hay un Avatar previo
                avatarViejo[0].delete()

            #_________________ Grabo avatar nuevo
            avatar = Avatar(user=u, imagen=form.cleaned_data['imagen'])
            avatar.save()

            #_________________ Almacenar en session la url del avatar para mostrarla en base
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session['avatar'] = imagen

            return render(request, "aplicacion/base.html")
    else:
        form = AvatarFormulario()
    return render(request, "aplicacion/agregarAvatar.html", {'form': form})


