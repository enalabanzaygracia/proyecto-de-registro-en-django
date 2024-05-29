from collections import OrderedDict
from unicodedata import category
from blog.models import Category



def get_categories(request):
    categories = Category.objects.values_list('id', 'name')  # Cambiar 'name' por el nombre del campo correcto
    return {
        'categories': categories
    }
