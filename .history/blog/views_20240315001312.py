from django.shortcuts import render
from blog.models import Category , Article
#from proyectoenDjango.blog.models import Article

# Create your views here.

def list(request):
    articles = Article.objects.all()
    return render(request, 'articles/list.html',{
        'title':'Articulos',
        'articles':articles
        
        
        })
    
def category(request,category_id):
    categories = Category.objects.get(id=category_id)
    re