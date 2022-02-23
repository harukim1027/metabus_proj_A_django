from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import (
    TokenObtainPairView as OriginTokenObtainPairView,
    TokenRefreshView as OriginTokenRefreshView,
)

from accounts.serializers import TokenObtainPairSerializer, UserCreationSerializer, UserSerializer
from notice.paginations.Pagination import Pagination

# email 전송을 위한 import 추가
from django.core.mail.message import EmailMessage

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = Pagination

    def get_queryset(self):
        qs = super().get_queryset()

        query = self.request.query_params.get("query", "")
        if query:
            qs = qs.filter(userID__icontains=query) or qs.filter(nickname__icontains=query) or qs.filter(
                name__icontains=query)

        return qs


class SignupAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreationSerializer
    permission_classes = [AllowAny]


class TokenObtainPairView(OriginTokenObtainPairView):
    serializer_class = TokenObtainPairSerializer


class TokenRefreshView(OriginTokenRefreshView):
    pass


# 메시지 전송 테스트
def send_email(request):
    subject = "message"
    to = ["metabusemail@gmail.com"]
    from_email = "metabusemail@gmail.com"
    message = "메지시 테스트"
    EmailMessage(subject=subject, body=message, to=to, from_email=from_email).send()
