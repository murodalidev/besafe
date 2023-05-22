from django.contrib import admin
from .models import Relationship, Contact


@admin.register(Relationship)
class RelationshipAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_other')
    list_filter = ('is_other', )
    search_fields = ('title', )


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'relationship', 'name', 'phone', 'created_date')
    list_filter = ('created_date', 'relationship')
    date_hierarchy = 'created_date'
    search_fields = ('author__phone', 'author__first_name', 'author__last_name', 'relationship')
