"""
Serializers available in the app.
"""

from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Message


class MessageSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(source="user",
                                                 queryset=User.objects.filter(is_superuser=False))

    class Meta:
        model = Message
        fields = ('id', 'text', 'user_id',)
        read_only_fields = ('id',)
