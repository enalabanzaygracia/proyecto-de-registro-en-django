from django.urls import path

from . import views

urlpatterns = [
     path('pagina/<str:slug>', views.page, name='page'),
       
]

    #path('admin/', admin.site.urls),
   # path('', views.index, name='index'),
   # path('inicio/', views.index, name='inicio'),


    #path('nosotros/', views.about, name='about'),
    


