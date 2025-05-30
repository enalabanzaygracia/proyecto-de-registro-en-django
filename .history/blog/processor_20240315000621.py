
from blog.models import Article, Category



def get_categories(request):
    
    ids=Article.objects.filter(public=True).values_list('categories', flat=True)
    
    
    categories = Category.objects.filter(id__in=).values_list('id', 'name') 
    return {
        'categories': categories,
        ids:ids
    }
