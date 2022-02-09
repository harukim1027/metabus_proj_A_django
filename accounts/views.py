from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import (
    TokenObtainPairView as OriginTokenObtainPairView,
    TokenRefreshView as OriginTokenRefreshView,
)
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.contrib import messages

from accounts.models import User
from accounts.serializers import TokenObtainPairSerializer, UserCreationSerializer, UserSerializer


class AccountsViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



Users = get_user_model()


class SignupAPIView(CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserCreationSerializer
    permission_classes = [AllowAny]


class TokenObtainPairView(OriginTokenObtainPairView):
    serializer_class = TokenObtainPairSerializer


class TokenRefreshView(OriginTokenRefreshView):
    pass



