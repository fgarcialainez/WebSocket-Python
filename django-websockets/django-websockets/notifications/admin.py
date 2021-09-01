from django.contrib import admin
from .models import WebsocketClient, Message


class WebsocketClientAdmin(admin.ModelAdmin):
    list_display = ['user', 'channel_name', 'created_at']


class MessageAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at', 'delivered']


admin.site.register(WebsocketClient, WebsocketClientAdmin)
admin.site.register(Message, MessageAdmin)
