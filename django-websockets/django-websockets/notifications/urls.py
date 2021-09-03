"""
Define urls available in the app.
"""

from django.urls import path
from rest_framework.authtoken import views

from .views import MessageCreateView

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token,  name='api-token-auth'),
    path('messages', MessageCreateView.as_view(), name='message-create'),
]
