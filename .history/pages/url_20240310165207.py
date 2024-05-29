from django.urls import path
from . import views

urlpatterns = [

    path('pagina/<str:slug>', pages_views.page, name='page'),
]


