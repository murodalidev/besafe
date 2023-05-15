from django.contrib import admin
from apps.blog.models import Category, Blog, BlogImage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title', )


class BlogImageInlineAdmin(admin.TabularInline):
    model = BlogImage
    fields = ('image', 'is_main')
    extra = 1


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    inlines = (BlogImageInlineAdmin, )
    list_display = ('id', 'title', 'category', 'created_date')
    date_hierarchy = 'created_date'
    list_filter = ('created_date', 'category')
