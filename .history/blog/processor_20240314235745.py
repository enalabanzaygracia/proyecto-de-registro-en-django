
from blog.models import Article, Category



def get_categories(request):
    
    ids=Article
    
    
    categories = Category.objects.values_list('id', 'name') 
    return {
        'categories': categories
    }
