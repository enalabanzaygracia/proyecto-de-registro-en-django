from collections import OrderedDict
from blog.models import Page

def get_pages(request):
    pages = Page.objects.filter(visible=True).order_by('order').values_list('id', 'title', 'slug')
    return {
        'pages': pages
    }