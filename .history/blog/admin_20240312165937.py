from typing import Any
from django.contrib import admin
from .models import Category, Article

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('user','created_at', 'updated_at')  
    def save_model(self, request, obj , form, change):
        if not obj.user_id:
            obj.user_id = request.user.id
        obj.save()    
        

admin.site.register(Category, )
admin.site.register(Article, ArticleAdmin)
