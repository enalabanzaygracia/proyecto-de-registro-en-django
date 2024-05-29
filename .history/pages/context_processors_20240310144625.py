from pages.models import Page

def get_pages(request):
    pages = Page.objects.filter(visiblevalues_list('id', 'title', 'slug')
    return {
        'pages': pages
    }