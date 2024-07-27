from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path("new-user", views.createUser),
    path("login", views.loginUser),
    path("logout", views.logout),
    path("coins", views.listAllCoins),
    path("categories", views.listAllCoinCategories),
    path("market-data", views.marketDataForCoin),
]
