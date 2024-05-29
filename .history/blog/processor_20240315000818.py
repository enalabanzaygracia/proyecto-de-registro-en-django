
from blog.models import Article, Category



def get_categories(request):
    
    categories_in_=Article.objects.filter(public=True).values_list('categories', flat=True)
    
    
    categories = Category.objects.filter(id__in=ids).values_list('id', 'name') 
    return {
        'categories': categories,
        ids:ids
    }
