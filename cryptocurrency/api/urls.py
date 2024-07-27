from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
path('', views.getData),
path('new-user', views.createUser),
path('login', views.loginUser)
]