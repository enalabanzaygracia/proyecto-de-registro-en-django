
#import statistics
from django.contrib import admin
from django.urls import path, include
from aplicacion import views
from pages import views as pages_views
#from blog import views as blog_views
from pages import views as pages_views
from django.conf import settings



urlpatterns = [
    path('admin/',  admin.site.urls),
    path('', include('aplicacion.url')),
    path('', include('pages.url')),
    path('', include('blog.url')),
    #path('', include('articulos.url')),

    
]


if settings.DEBUG:  
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



