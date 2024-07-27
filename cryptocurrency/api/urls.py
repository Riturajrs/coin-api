from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path("new-user", views.createUser),
    path("login", views.loginUser),
    path("logout", views.logout),
    path("coins", views.listAllCoins, name="list_all_coins"),
    path("categories", views.listAllCoinCategories),
    path("market-data", views.marketDataForCoin),
]
