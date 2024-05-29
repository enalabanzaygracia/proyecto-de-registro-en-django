from collections import OrderedDict
from unicodedata import category
from blog.models import Category

def get_categories(request):
    categories = v.objects.filter(visible=True).order_by('order').values_list('id', 'title', 'slug')
    return {
        'pages': from collections import OrderedDict
from pages.models import Page

def get_pages(request):
    pages = Page.objects.filter(visible=True).order_by('order').values_list('id', 'title', 'slug')
    return {
        'pages': pages
    }
    }