from collections import OrderedDict
from blog.models import Category

def get_categories(request):
    c = Page.objects.filter(visible=True).order_by('order').values_list('id', 'title', 'slug')
    return {
        'pages': pages
    }