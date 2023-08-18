from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MotoForm(forms.Form):
    marca = forms.CharField(label="Nombre de la Moto", max_length=50, required=True)
    modelo = forms.IntegerField(label="Modelo", required=True)
    Origen = forms.EmailField(label="Origen", required=False)
    ESTILOS = (
        (1, "Scrambler"),
        (2, "Sport"),
        (3, "Naked"),
    )
    estilo = forms.ChoiceField(label="Estilo elegido", choices=ESTILOS, required=True)
    vehiculo = forms.BooleanField()

class AccesorioForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=50, required=True)
    modelo = forms.CharField(label="Modelo", max_length=50, required=True)
    origen = forms.EmailField(label="Origen")
    vehiculo = forms.CharField(label="vehiculo", max_length=50, required=True)

class RegistroUsuariosForm(UserCreationForm):
    email = forms.EmailField(label="Email Usuario")
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}    

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar E-mail")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 
    first_name = forms.CharField(label="Nombre/s", max_length=50, required=False)
    last_name = forms.CharField(label="Apellido/s", max_length=50, required=False)

    class Meta:
        model = User
        fields = [ 'email', 'password1', 'password2', 'first_name', 'last_name' ] 
        #Saca los mensajes de ayuda
        help_texts = { k:"" for k in fields}

class AvatarFormulario(forms.Form):
    imagen = forms.ImageField(required=True)        