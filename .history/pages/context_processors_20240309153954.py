from pages.models import Page

def get_pages(request):
    pages = Page.objects.values_list('title','content').order_by('title')