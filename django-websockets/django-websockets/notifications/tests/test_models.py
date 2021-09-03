"""
This module holds all the tests related to the app models.
"""

from django.contrib.auth.models import User
from django.test import TestCase

from ..models import Message, WebsocketClient


class ModelsTests(TestCase):
    """Tests for the models available in the app"""

    def _create_sample_user(self):
        return User.objects.create_user(
            email='test@test.com',
            username='test',
            password='Password123'
        )

    def test_create_user(self):
        """Test create user model"""
        user = self._create_sample_user()

        self.assertEqual(str(user), user.username)

    def test_create_message(self):
        """Test create message model"""
        user = self._create_sample_user()

        message = Message.objects.create(text="test", user=user)

        self.assertEqual(str(message), message.text)

    def test_create_websocket_client(self):
        """Test create message model"""
        user = self._create_sample_user()

        client = WebsocketClient.objects.create(channel_name="test_channel_name", user=user)

        self.assertEqual(str(client), client.channel_name)

