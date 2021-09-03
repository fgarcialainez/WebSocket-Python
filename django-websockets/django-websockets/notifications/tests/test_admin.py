"""
This module holds all the tests related to the admin site.
"""

from django.urls import reverse
from rest_framework import status

from .test_base import BaseApiTests


class AdminSiteTests(BaseApiTests):
    """Tests for the urls available in the admin console"""

    def setUp(self):
        super().setUp()

        # Login the superuser
        self.client.force_login(self.admin_user)

    def test_users_list(self):
        """Test that users are listed in the admin console"""
        url = reverse('admin:auth_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.email)
        self.assertContains(res, self.user.username)

    def test_messages_list(self):
        """Test that messages are listed in the admin console"""
        url = reverse('admin:notifications_message_changelist')
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_websocketclient_list(self):
        """Test that WebSocket clients are listed in the admin console"""
        url = reverse('admin:notifications_websocketclient_changelist')
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
