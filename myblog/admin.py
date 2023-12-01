from django.contrib import admin
from .models import Post, Dawlet, Category

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','firstname']
    ordering = ['-id']
    search_fields = ['firstname']

@admin.register(Dawlet)
class DawletAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    ordering = ['-id']
    search_fields = ['name']
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    ordering = ['-id']
    search_fields = ['name']
# @admin.register(Categories)
# class CategoriesAdmin(admin.ModelAdmin):
#     list_display = ['id','name']
#     ordering = ['-id']
#     search_fields = ['name']

    