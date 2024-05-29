
from blog.models import Article, Category



def get_categories(request):
    
    ids=Article.objects.filter(public=True).values_list('category_id', flat=True)
    
    
    categories = Category.objects.values_list('id', 'name') 
    return {
        'categories': categories
    }
