"""
This module holds all the tests related to the create messages API endpoint.
"""

from django.urls import reverse
from rest_framework import status

from .test_base import BaseApiTests

# Define Urls to test
CREATE_MESSAGE_URL = reverse('message-create')


class CreateMessagesApiTests(BaseApiTests):
    """Tests for the create messsages API endpoint"""

    def test_create_message_success(self):
        """Test to check the create message API endpoint with success"""

        # Check the create message endpoint
        payload = {
            'text': 'Test message',
            'user_id': self.user.id
        }

        res = self.client.post(CREATE_MESSAGE_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_create_message_forbidden(self):
        """Test to check the create message API endpoint forbidden"""

        # Authenticate a regular user
        self.client.force_authenticate(self.user)

        # Check the create message endpoint
        payload = {
            'text': 'Test message',
            'user_id': self.user.id
        }

        res = self.client.post(CREATE_MESSAGE_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_message_invalid_user(self):
        """Test to check the create message API endpoint invalid user"""

        # Check the create message endpoint
        payload = {
            'text': 'Test message',
            'user_id': 100  # <- Invalid user identifier
        }

        res = self.client.post(CREATE_MESSAGE_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
