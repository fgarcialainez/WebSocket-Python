"""
Models available in the app.
"""

from django.db import models
from django.contrib.auth.models import User


class WebsocketClient(models.Model):
    channel_name = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now=True, editable=False, null=True)
    user = models.OneToOneField(User, related_name='wsclient', on_delete=models.CASCADE,
                                limit_choices_to={'is_superuser': False})


class Message(models.Model):
    text = models.CharField(max_length=1024)
    delivered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True, editable=False, null=True)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE,
                             limit_choices_to={'is_superuser': False})
