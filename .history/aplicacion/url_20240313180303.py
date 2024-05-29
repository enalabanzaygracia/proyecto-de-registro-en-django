from msilib.schema import AdminExecuteSequence



from django.urls import path , include

import views 

urlpatterns = [
    path('admin/', AdminExecuteSequence.site.urls),
    path('', include ,(' aplicacion.urls')),
    path('', include , ('pages.urls')),
    path('', include , ('blog.urls')),

]
if settings.DEBUG:
  from django.conf.urls.static import static 
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)