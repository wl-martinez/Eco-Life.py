from django.shortcuts import render
from sympy import re
from .models import Producto

# Create your views here.

def productos(request):
    productos = Producto.objects.all()
    data = {
         'productos': productos
    }
    return render(request, 'app/productos.html', data)

def carrito(request):
    return render(request, 'app/carrito.html')

def ingresar(request):
    return render(request, 'app/ingresar.html')

def index(request):
    return render(request, 'app/index.html')

