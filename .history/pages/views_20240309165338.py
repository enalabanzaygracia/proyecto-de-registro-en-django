from django.shortcuts import render

# Create your views here.
def page(request):
    
    title: " pagina individual ",
    page 
    
    
    return render(request, "pages/page.html", 
                  {"page":"hola le saluda jesus andres desde la app pages"} )