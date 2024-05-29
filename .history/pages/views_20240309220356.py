from django.shortcuts import render
from .models import Page

def page(request, slug):
    page= page.objects.get(slug=slug)
    
    return render(request, "pages/page.html", {
        'title': "Página individual",
        'page': page
            
            
            "Hola, te saluda Jesús Andrés desde la app pages"
    })
