from django.shortcuts import render, HttpResponse

# Create your views here.
def principal(request):
    return HttpResponse("<h1>Prueba</h1><h2>Portada</h2>")