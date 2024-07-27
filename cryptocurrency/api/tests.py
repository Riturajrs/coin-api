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
        self.url = reverse("list-all-coins")

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


class ListAllCategoriesTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.token, _ = Token.objects.get_or_create(user=self.user)

        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
        self.url = reverse("list-all-categories")

    @patch("requests.get")
    def test_list_all_coins_success(self, mock_get):
        mock_categories = [
            {"category_id": "beamprivacy-ecosystem", "name": "BeamPrivacy Ecosystem"},
            {"category_id": "berachain-ecosystem", "name": "Berachain Ecosystem"},
            {"category_id": "bevm-ecosystem", "name": "BEVM Ecosystem"},
            {"category_id": "big-data", "name": "Big Data"},
            {
                "category_id": "binance-hodler-airdrops",
                "name": "Binance HODLer Airdrops",
            },
        ]
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_categories

        response = self.client.get(self.url, {"page_num": 1, "per_page": 2})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["category_id"], "beamprivacy-ecosystem")
        self.assertEqual(response.data[1]["category_id"], "berachain-ecosystem")

    @patch("requests.get")
    def test_list_all_coins_pagination(self, mock_get):
        mock_categories = [
            {"category_id": "beamprivacy-ecosystem", "name": "BeamPrivacy Ecosystem"},
            {"category_id": "berachain-ecosystem", "name": "Berachain Ecosystem"},
            {"category_id": "bevm-ecosystem", "name": "BEVM Ecosystem"},
            {"category_id": "big-data", "name": "Big Data"},
            {
                "category_id": "binance-hodler-airdrops",
                "name": "Binance HODLer Airdrops",
            },
        ]

        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_categories
        response = self.client.get(self.url, {"page_num": 2, "per_page": 2})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["category_id"], "bevm-ecosystem")

    @patch("requests.get")
    def test_list_all_coins_error(self, mock_get):
        mock_get.return_value.status_code = 500
        mock_get.return_value.raise_for_status.side_effect = (
            requests.exceptions.RequestException("Test error")
        )

        response = self.client.get(self.url, {"page_num": 1, "per_page": 2})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("An error occurred: Test error", response.data)


class MarketDataForCoinTest(APITestCase):
    def setUp(self):
        # Set up a test user and get a token
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.token, _ = Token.objects.get_or_create(user=self.user)

        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
        self.url = reverse("market-data-for-coin")

    @patch("requests.get")
    def test_market_data_for_coin_with_id_and_category(self, mock_get):
        mock_market_data = [
            {"id": "bitcoin", "symbol": "btc", "name": "Bitcoin"},
            {"id": "ethereum", "symbol": "eth", "name": "Ethereum"},
        ]
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_market_data

        response = self.client.get(
            self.url,
            {
                "page_num": 1,
                "per_page": 2,
                "id": "bitcoin",
                "category": "cryptocurrency",
            },
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["id"], "bitcoin")
        self.assertEqual(response.data[1]["id"], "ethereum")

    @patch("requests.get")
    def test_market_data_for_coin_with_id_only(self, mock_get):
        mock_market_data = [{"id": "bitcoin", "symbol": "btc", "name": "Bitcoin"}]
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_market_data

        response = self.client.get(
            self.url, {"page_num": 1, "per_page": 1, "id": "bitcoin"}
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["id"], "bitcoin")

    @patch("requests.get")
    def test_market_data_for_coin_with_category_only(self, mock_get):
        mock_market_data = [{"id": "ethereum", "symbol": "eth", "name": "Ethereum"}]
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_market_data

        response = self.client.get(
            self.url, {"page_num": 1, "per_page": 1, "category": "cryptocurrency"}
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["id"], "ethereum")

    @patch("requests.get")
    def test_market_data_for_coin_pagination(self, mock_get):
        mock_market_data = [
            {"id": "bitcoin", "symbol": "btc", "name": "Bitcoin"},
            {"id": "ethereum", "symbol": "eth", "name": "Ethereum"},
            {"id": "ripple", "symbol": "xrp", "name": "Ripple"},
        ]
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_market_data

        response = self.client.get(
            self.url, {"page_num": 2, "per_page": 2, "category": "cryptocurrency"}
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["id"], "ripple")

    @patch("requests.get")
    def test_market_data_for_coin_error(self, mock_get):
        mock_get.return_value.status_code = 500
        mock_get.return_value.raise_for_status.side_effect = (
            requests.exceptions.RequestException("Test error")
        )

        response = self.client.get(
            self.url,
            {
                "page_num": 1,
                "per_page": 2,
                "id": "bitcoin",
                "category": "cryptocurrency",
            },
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("An error occurred: Test error", response.data)


class GetHealthCheckTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.token, _ = Token.objects.get_or_create(user=self.user)

        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
        self.url = reverse("get-health-check")

    @patch("requests.get")
    def test_get_health_check_success(self, mock_get):
        mock_response = {"gecko_says": "(V3) To the Moon!"}
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["version"], 1.0)
        self.assertEqual(response.data["status"], "online")
        self.assertEqual(response.data["3rd party api response"], str(mock_response))

    @patch("requests.get")
    def test_get_health_check_error(self, mock_get):
        mock_get.side_effect = requests.exceptions.RequestException("Test error")

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertIn("An error occurred: Test error", response.data)


if __name__ == "__main__":
    import unittest

    unittest.main()
