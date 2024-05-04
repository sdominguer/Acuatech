
from django.http import HttpResponse

# Create your views here.

from django.shortcuts import render, redirect
from .models import Product, ItemCarrito
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.forms import AuthenticationForm

def index(request):
    return render(request, "index.html")

def usuario(request):
    return render(request, "usuario.html")


def signupaccounts(request):
    if request.method == "GET":
        return render(request, "signupaccounts.html", {"form":UserCreationForm})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(request.POST["username"], password=request.POST["password1"])
                print(user)
                user.save()
                login(request, user)
                return redirect("../home")
            except IntegrityError:
                return render(request, "signupaccounts.html", {"form":UserCreationForm, "error":"Username already taken. Choose new username. "})

        else:
            return render(request, "signupaccounts.html", {"form":UserCreationForm, "error":"Passwords do not match"})




def carrito(request):
    # Obtener el carrito de la sesión del usuario
    carrito = request.session.get('carrito', {})
    items_carrito = []

    # Obtener todos los productos en el carrito y calcular el precio total
    total_precio = 0
    for producto_id, cantidad in carrito.items():
        producto = Product.objects.get(id=producto_id)
        precio_total_producto = producto.precio * cantidad
        total_precio += precio_total_producto
        items_carrito.append({'producto': producto, 'cantidad': cantidad, 'precio_total': precio_total_producto})

    return render(request, 'carrito.html', {'items_carrito': items_carrito, 'total_precio': total_precio})

def agregar_al_carrito(request, producto_id):
    # Obtener el carrito de la sesión del usuario
    carrito = request.session.get('carrito', {})
    
    # Obtener el producto a agregar al carrito
    producto = Product.objects.get(id=producto_id)

    # Agregar el producto al carrito o incrementar su cantidad si ya está en el carrito
    carrito[producto_id] = carrito.get(producto_id, 0) + 1

    # Guardar el carrito en la sesión del usuario
    request.session['carrito'] = carrito

    return redirect('carrito')

def eliminar_del_carrito(request, producto_id):
    # Obtener el carrito de la sesión del usuario
    carrito = request.session.get('carrito', {})
    
    # Eliminar el producto del carrito
    if producto_id in carrito:
        del carrito[producto_id]

    # Guardar el carrito actualizado en la sesión del usuario
    request.session['carrito'] = carrito

    return redirect('carrito')


def logoutaccount(request):
    logout(request)
    return redirect('index') 


def home(request):
    return render(request, "home.html")

def servicios(request):
    return render(request, "servicios.html")

def tienda(request):
    products = Product.objects.all()
    return render(request, 'tienda.html', {'products': products})



def loginaccount(request):
    if request.method == "GET":
        return render(request, "loginaccount.html", {'form': AuthenticationForm})
    else:
        user= authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'loginaccount.html', {'form': AuthenticationForm(), 'error':"username and password do not match"})
        else:
            login(request,user)
            return redirect("../home")
