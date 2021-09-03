"""
This module holds the common code for the API tests.
"""

from rest_framework.test import APITestCase

from django.contrib.auth.models import User


class BaseApiTests(APITestCase):
    """Base class for API related tests"""

    def setUp(self):
        # Create an admin user and a regular user for testing
        self.admin_user = User.objects.create_superuser(
            email='testadmin@test.com',
            username='testadmin',
            password='password123'
        )

        self.user = User.objects.create_user(
            email='testuser@test.com',
            username='testuser',
            password='password123',
        )

        # Authenticate the superuser
        self.client.force_authenticate(self.admin_user)
