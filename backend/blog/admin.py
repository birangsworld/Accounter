from django.contrib import admin

from .models import Article, Category, Tag


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at', 'is_active')
    list_filter = ('created_at', 'updated_at', 'is_active')
    search_fields = ('name',)
    
admin.site.register(Category, CategoryAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'content', 'category__name', 'created_at', 'updated_at', 'is_active')
    list_filter = ('created_at', 'updated_at', 'is_active', 'category__name')
    search_fields = ('title', 'description', 'content', 'category__name')
    
admin.site.register(Article, ArticleAdmin)

class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at', 'is_active')
    list_filter = ('created_at', 'updated_at', 'is_active')
    search_fields = ('name',)

admin.site.register(Tag, TagAdmin)