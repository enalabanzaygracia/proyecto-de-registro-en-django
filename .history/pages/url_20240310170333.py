from django.urls import path
import views

urlpatterns = [
   # path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('inicio/', views.index, name='inicio'),
    #path('nosotros/', views.about, name='about'),
    path('pagina/<str:slug>', pages_views.page, name='page'),
]


