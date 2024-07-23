from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Prueba</h1><h2>Portada</h2>")

def about(request):
    return HttpResponse("<h1>About me:</h1><p1>Hello, my name is Ricardo Gobbi and I'm a Python developer.</p1>")

def portfolio(request):
    return HttpResponse("<h1>My projects</h1><p1>This are my projects:</p1>")

def contact(request):
    return HttpResponse("<h1>Contacto</h1><p1>ricky.gobbi1994@gmail.com</p1>")