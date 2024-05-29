from turtle import title
from django.contrib import admin
from .models import Page

admin.site.register(Page)




#configuraciond el panel


title = "Panel de Administracion proyecto Django desde admin.py title"
subtitle = "Panel de Gestion proyecto Django desde admin.py subtitle"


admin.site.site_header = title
admin.site.site_title = subtitle
admin.site.index_title = "Bienvenido al Panel de Administracion desde a"