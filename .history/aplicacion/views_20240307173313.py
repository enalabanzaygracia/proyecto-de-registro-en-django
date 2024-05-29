from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'aplicacion/index.html',{'title':'inicio'})

def about(request):
    return render(request, 'aplicacion/about.html',{'title':'Sobre Nosotros'})  