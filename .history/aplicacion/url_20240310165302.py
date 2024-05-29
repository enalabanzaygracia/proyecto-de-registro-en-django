from django.urls import path
from . import views

urlpatterns = [

    path('pagina/<str:slug>', views.page, name='page'),
    path('', views.index, name='index'),
    path('inicio/', views.index, name='inicio'),
]


