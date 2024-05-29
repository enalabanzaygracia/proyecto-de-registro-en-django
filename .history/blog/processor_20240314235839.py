
from blog.models import Article, Category



def get_categories(request):
    
    ids=Article.objects.filter(pu)
    
    
    categories = Category.objects.values_list('id', 'name') 
    return {
        'categories': categories
    }
