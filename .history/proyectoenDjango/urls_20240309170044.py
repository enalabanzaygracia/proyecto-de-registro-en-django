
from django.contrib import admin
from django.urls import path
from aplicacion import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('inicio/', views.index, name='inicio'),
    #path('nosotros/', views.about, name='about'),
    
]


