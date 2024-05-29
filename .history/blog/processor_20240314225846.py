from collections import OrderedDict
from unicodedata import category
from blog.models import Category

def get_categories(request):
    categories = category.objects.values_list('id', 'title', 'slug')
    return {
        'pages': category
    }