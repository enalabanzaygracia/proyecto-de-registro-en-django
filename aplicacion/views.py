from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from aplicacion.forms import RegisterForm

# Create your views here.
def index(request):
    return render(request, 'aplicacion/index.html',{'title':'inicio'})

def about(request):
    return render(request, 'aplicacion/about.html',{'title':'Sobre Nosotros'})  


def register_page(request):
    register_form = RegisterForm()


    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()

            return redirect('inicio')
        else:
            print('Error al registrar')




    return render(request, 'user/register.html',{
       'title':'Registro',
       'register_form': register_form
    })
    