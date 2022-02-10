from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import (
    TokenObtainPairView as OriginTokenObtainPairView,
    TokenRefreshView as OriginTokenRefreshView,
)
from accounts.models import User
from accounts.serializers import TokenObtainPairSerializer, UserCreationSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

User = get_user_model()


class SignupAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreationSerializer
    permission_classes = [AllowAny]


class TokenObtainPairView(OriginTokenObtainPairView):
    serializer_class = TokenObtainPairSerializer


class TokenRefreshView(OriginTokenRefreshView):
    pass



