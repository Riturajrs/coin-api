from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path("new-user", views.createUser),
    path("login", views.loginUser),
    path("logout", views.logout),
    path("coins", views.listAllCoins, name="list-all-coins"),
    path("categories", views.listAllCoinCategories, name="list-all-categories"),
    path("market-data", views.marketDataForCoin, name="market-data-for-coin"),
    path("health",views.getHealthCheck, name="get-health-check"),
]
