urlpatterns = [
    path('admin/', admin.site.urls),
    path('aplicacion/', include('aplicacion.urls')),
    path('pages/', include('pages.urls')),
]
