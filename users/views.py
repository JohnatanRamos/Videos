""" Esto hace que cuando se ingrese, primero verifique
con el metodo authenticate si es correcto entra al metodo login"""
from django.contrib.auth import authenticate, login, logout
# render es un metodo que toma un request
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# My models
from users.models import Profile
# Para crear un usuario con el modelo que trea django por defecto
from django.contrib.auth.models import User

# exception
from django.db.utils import IntegrityError


def view_login(request):
    # Verificamos que el request use el metodo post
    if request.method == 'POST':
        # Recibimos el username y el password
        username = request.POST['inputUser']
        password = request.POST['inputPassword']
        # Con el metodo authenticate verificamos los datos del usuario
        user = authenticate(request, username=username, password=password)
        if user:
            # Si la verificacion es correcta, llamamos el metodo login, que va abrir la seccion
            login(request, user)
            # Renderizamos a la vista post
            return redirect('Post')
        else:
            # Si los datos son incorrectos se envia nuevamente al Login
            return render(request, 'User/login.html', {'error': 'User and password incorrect'})
    return render(request, 'User/login.html')


"""@login_required
def view_logout(request):
    logout(request)
    return render(request,'User/login.html')


"""
@login_required
def view_logout(request):
    logout(request)
    return redirect('Login')


def view_sing_up(request):
    if request.method == 'POST':
        username = request.POST['inputUserN']
        password = request.POST['inputPassword']
        confirm = request.POST['inputConfirm']

        if confirm != password:
            return render(request, 'User/sign_up.html', {'error': 'La contraseña no coincide'})

        # try catch para que no se dañe si se pasa un username que ya existe
        try:
            # Le pasamos las variables que recibimos al modelo user de django
            user = User.objects.create_user(username=username, password=password)
        except IntegrityError:
            return render(request, 'User/sign_up.html', {'error': 'El nombre de usuario ya esta en uso'})

        # Le pasamos las variables que recibimos al modelo user de django
        user.first_name = request.POST['inputFName']
        user.last_name = request.POST['inputLName']
        user.email = request.POST['inputEmail']
        user.save()

        # Como el model profile tiene la PK del modelo user de django se le pasa lo que tiene a profile
        profile = Profile(user=user)
        profile.save()
        return redirect('Login')

    return render(request, 'User/sign_up.html')