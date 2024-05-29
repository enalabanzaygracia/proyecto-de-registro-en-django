
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]




from aplicacion import views


    path('', views.index, name="inidex" ),
    path('inicio/', views.index, name="inicio" ),
    path('nosotros/', views.about, name="nosotros" ),