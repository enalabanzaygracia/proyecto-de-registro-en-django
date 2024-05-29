from django.shortcuts import render
from .models import Page

def page(request, slug):
    page_obj = Page.objects.get(slug=slug)  # Corregido el nombre de la variable y el uso de Page
    return render(request, "pages/page.html", {
        'title': "Página individual",
        'page': page_obj  # Corregido el nombre de la variable
    })
