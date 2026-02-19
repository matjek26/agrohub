from django.contrib import admin
from .models import ChatMessage

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('session_id', 'user', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('message', 'response', 'session_id')
