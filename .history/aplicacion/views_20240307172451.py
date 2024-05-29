from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'miapp/index.html',{'title':'inicio'})

def about(request):
    return render(request, 'miapp/about.html',{'title':'Sobre Nosotros'})   from django.apps import AppConfig