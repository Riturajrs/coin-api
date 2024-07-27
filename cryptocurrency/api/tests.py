from django.contrib.auth.models import User
import requests
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from rest_framework import status
from unittest.mock import patch
from django.urls import reverse


class ListAllCoinsTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.token, _ = Token.objects.get_or_create(user=self.user)

        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
        self.url = reverse("list_all_coins")

    @patch("requests.get")
    def test_list_all_coins_success(self, mock_get):
        mock_coins = [
            {"id": "bitcoin", "symbol": "btc", "name": "Bitcoin"},
            {"id": "ethereum", "symbol": "eth", "name": "Ethereum"},
        ]
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_coins

        response = self.client.get(self.url, {"page_num": 1, "per_page": 2})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["id"], "bitcoin")
        self.assertEqual(response.data[1]["id"], "ethereum")

    @patch("requests.get")
    def test_list_all_coins_pagination(self, mock_get):
        mock_coins = [
            {"id": "bitcoin", "symbol": "btc", "name": "Bitcoin"},
            {"id": "ethereum", "symbol": "eth", "name": "Ethereum"},
            {"id": "ripple", "symbol": "xrp", "name": "Ripple"},
        ]
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_coins

        response = self.client.get(self.url, {"page_num": 2, "per_page": 2})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["id"], "ripple")

    @patch("requests.get")
    def test_list_all_coins_error(self, mock_get):
        mock_get.return_value.status_code = 500
        mock_get.return_value.raise_for_status.side_effect = (
            requests.exceptions.RequestException("Test error")
        )

        response = self.client.get(self.url, {"page_num": 1, "per_page": 2})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("An error occurred: Test error", response.data)


if __name__ == "__main__":
    import unittest

    unittest.main()
