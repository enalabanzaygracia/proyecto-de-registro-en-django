
from blog.models import Category



def get_categories(request):
    
    ids=art
    
    
    categories = Category.objects.values_list('id', 'name') 
    return {
        'categories': categories
    }
