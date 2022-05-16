from django.shortcuts import render
from sympy import re

# Create your views here.

def index(request):
    return render(request, 'app/index.html')

def carrito(request):
    return render(request, 'app/carrito.html')

def ingresar(request):
    return render(request, 'app/ingresar.html')

def productos(request):
    return render(request, 'app/productos.html')

