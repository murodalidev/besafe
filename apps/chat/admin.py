from django.contrib import admin
from apps.chat.models import Chat, ChatMember, Message, Media


class ChatMemberInline(admin.TabularInline):
    model = ChatMember
    extra = 0


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    inlines = (ChatMemberInline, )
    list_display = ('id', 'is_deleted', 'type', 'messages_count', 'created_date')
    list_filter = ('created_date', 'is_deleted', 'type')
    date_hierarchy = 'created_date'
    search_fields = ('chat_members__first_name', 'chat_members__last_name', 'chat_members__phone')
    list_per_page = 25


@admin.register(ChatMember)
class ChatMemberInline(admin.ModelAdmin):
    list_display = ('id', 'member', 'full_name')
    search_fields = ('member__first_name', 'member__last_name', 'member__phone')

    def full_name(self, obj):
        return obj.member.full_name


class MediaInline(admin.TabularInline):
    model = Media
    extra = 0


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    inlines = (MediaInline, )
    list_display = ('id', 'chat', 'sender', 'is_read', 'is_deleted', 'created_date')
    list_filter = ('created_date', 'is_deleted')
    date_hierarchy = 'created_date'
    search_fields = ('chat__id', )
    list_per_page = 25


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'message', 'is_deleted')
    list_filter = ('is_deleted', )
    search_fields = ('message__id', )
    list_per_page = 25


