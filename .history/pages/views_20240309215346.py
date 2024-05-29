from django.shortcuts import render
from .

def page(request):
    return render(request, "pages/page.html", {
        'title': "Página individual",
        'page': "Hola, te saluda Jesús Andrés desde la app pages"
    })
