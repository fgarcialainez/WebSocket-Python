"""
Views available in the app.
"""

from rest_framework import generics
from rest_framework import permissions

from .serializers import  MessageSerializer
from .models import Message


class MessageCreateView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAdminUser]
