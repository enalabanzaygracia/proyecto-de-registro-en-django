from django.shortcuts import render

# Create your views here.
def page(request):
    
    
    
    return render(request, "pages/page.html",{
        title: " pagina individual ",
        page : " pagina individual ",
        "page":"hola le saluda jesus andres desde la app pages"} )
        
    