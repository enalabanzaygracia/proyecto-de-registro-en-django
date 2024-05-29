from collections import OrderedDict
from unicodedata import category
from blog.models import Category

def get_categories(request):
    categories = category.objects.filter(visible=True).order_by('order').values_list('id', 'title', 'slug')
    return {
        'pages': category
    }