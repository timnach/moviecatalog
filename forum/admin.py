from django.contrib import admin
from .models import Forum, Message

class ForumAdmin(admin.ModelAdmin):
    list_display = ('title', 'film', 'created_at',)
    search_fields = ('title', 'description',)
    list_filter = ('film',)

class MessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'forum', 'created_at',)
    search_fields = ('user', 'text',)
    list_filter = ('forum', 'created_at', 'user')

admin.site.register(Forum, ForumAdmin)
admin.site.register(Message, MessageAdmin)