import requests
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .serializers import UserSerializer


@api_view(["POST"])
def createUser(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data["username"])
        user.set_password(request.data["password"])
        user.save()
        token = Token.objects.create(user=user)
        return Response(
            {"token": token.key, "user": serializer.data},
            status=status.HTTP_201_CREATED,
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def loginUser(request):
    user = authenticate(
        username=request.data["username"], password=request.data["password"]
    )
    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        serializer = UserSerializer(instance=user)
        return Response(
            {"token": token.key, "user": serializer.data}, status=status.HTTP_200_OK
        )
    else:
        return Response(
            {"message": "Wrong credentials!"}, status=status.HTTP_404_NOT_FOUND
        )


@api_view(["POST"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def logout(request):
    request.user.auth_token.delete()
    return Response(f"User {request.user.email} has been logged out!")


@api_view(["GET"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def testAuth(request):
    return Response(f"Authenticated user: {request.user.email} !")


@api_view(["GET"])
def listAllCoins(request):
    url = "https://api.coingecko.com/api/v3/coins/list"
    try:
        response = requests.get(url)

        response.raise_for_status()
        return Response(response.json(), status=status.HTTP_200_OK)
    except requests.exceptions.RequestException as error:
        return Response(
            {f"An error occurred: {error}"}, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["GET"])
def listAllCoinCategories(request):
    url = "https://api.coingecko.com/api/v3/coins/categories/list"

    try:
        response = requests.get(url)

        response.raise_for_status()
        return Response(response.json(), status=status.HTTP_200_OK)
    except requests.exceptions.RequestException as error:
        return Response(
            {f"An error occurred: {error}"}, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["GET"])
def marketDataForCoin(request):
    url = None
    if "id" in request.data and request.data["id"] is not None and "category" in request.data and request.data["category"] is not None:
        url = f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=cad&ids={request.data["id"]}&category={request.data["category"]}"
    elif "id" in request.data and request.data["id"] is not None:
        url = f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=cad&ids={request.data["id"]}"
    elif "category" in request.data and request.data["category"] is not None:
        url = f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=cad&category={request.data["category"]}"
    
    try:
        response = requests.get(url)

        response.raise_for_status()
        return Response(response.json(), status=status.HTTP_200_OK)
    except requests.exceptions.RequestException as error:
        return Response(
            {f"An error occurred: {error}"}, status=status.HTTP_400_BAD_REQUEST
        )
