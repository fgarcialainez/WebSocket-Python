"""
This module holds the tests for the Token authentication endpoint.
"""

from django.urls import reverse
from rest_framework import status

from .test_base import BaseApiTests

# Define Urls to test
CREATE_TOKEN_URL = reverse('api-token-auth')


class TokenAuthenticationApiTests(BaseApiTests):
    """Test the Token authentication API"""

    def test_create_token_for_user_success(self):
        """Test that a token is created for a regular user"""

        # Create the payload
        payload = {'username': self.user.username, 'password': 'password123'}

        res = self.client.post(CREATE_TOKEN_URL, payload)

        # Check result
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIn('token', res.data)

    def test_create_token_for_user_superuser_success(self):
        """Test that a token is created for a superuser"""

        # Create the payload
        payload = {'username': self.admin_user.username, 'password': 'password123'}

        res = self.client.post(CREATE_TOKEN_URL, payload)

        # Check result
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIn('token', res.data)

    def test_create_token_for_invalid_user_error(self):
        """Test that a token is not created for an invalid user"""

        # Create the payload
        payload = {'username': 'invaliduser', 'password': 'invalidpassword'}

        res = self.client.post(CREATE_TOKEN_URL, payload)

        # Check result
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_for_invalid_password_error(self):
        """Test that a token is not created for an invalid password"""

        # Create the payload
        payload = {'username': self.user.username, 'password': 'invalidpassword'}

        res = self.client.post(CREATE_TOKEN_URL, payload)

        # Check result
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
