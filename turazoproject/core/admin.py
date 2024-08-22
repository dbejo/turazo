from django.contrib import admin
from .models import Category, Post, Photo, Tag

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
admin.site.register(Category, CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
admin.site.register(Post, PostAdmin)

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
admin.site.register(Tag, TagAdmin)

admin.site.register(Photo)