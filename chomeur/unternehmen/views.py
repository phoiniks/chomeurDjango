from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("¡Hola, mundo! ¿Qué tal? Éste es el famoso Django.")
