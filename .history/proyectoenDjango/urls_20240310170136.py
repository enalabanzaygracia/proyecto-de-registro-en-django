from django.contrib import admin
from django.urls import path, include
#from aplicacion import views
#from pages import views as pages_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('aplicacion/', include('aplicacion.urls')),
    path('pages/', include('pages.urls')),
]
