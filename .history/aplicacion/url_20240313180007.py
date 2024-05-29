from msilib.schema import AdminExecuteSequence
from django.conf import settings
from django.urls import path , include
import views 

urlpatterns = [
    path('admin/', AdminExecuteSequence.site.urls),
    path('', include ,(' aplicacion.urls')),
    path('', include , ('pages.urls')),
    path('', include , ('blog.urls')),

]
if settings.DEBUG:
  from dj

