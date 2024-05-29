from django.urls import path
import views

urlpatterns = [

    path('pagina/<str:slug>', pages_views.page, name='page'),
]


