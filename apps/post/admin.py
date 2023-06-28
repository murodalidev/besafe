from django.contrib import admin

from apps.post.models import Post, PostImage, Comment



class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 0


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = (PostImageInline, )
    list_display = ('id', 'author', 'modified_date', 'created_date')
    date_hierarchy = 'created_date'
    list_filter = ('created_date',)
    search_fields = ('author__first_name', 'author__last_name')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'post', 'parent_comment', 'top_level_comment_id', 'created_date')
    date_hierarchy = 'created_date'
    list_filter = ('created_date',)
    search_fields = ('author__first_name', 'author__last_name', 'top_level_comment_id')
    search_help_text = 'search fields: author, top_level_comment_id'

