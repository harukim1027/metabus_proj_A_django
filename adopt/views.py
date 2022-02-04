import json

from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet  # <-- 아랫줄 하나하나가 다 포함되있는 부모
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveAPIView,
)
from adopt.models import Review
from adopt.serializers import (
    ReviewSerializer,
)  # ArticleAnonymousSerializer, ArticleGoldMembershipSerializer,


# list, detail, create, update, delete 를 1개 ViewSet에서 지원
# 나눠서 리스트, 디테일은 아무때나 조회 가능, 나머지는 인증 됐을 때만
# request type에 따라
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # permission_classes = [AllowAny]  # DRF 디폴트 설정
    # permission_classes = [IsAuthenticated]
    # 위 주석 한줄과 아래는 같은 결과

    def get_permissions(self):
        # if self.request.method in ("POST", "PUT", "PATCH", "DELETE"):
        if self.request.method == "GET":
            # 각각을 언제 쓰느냐를 잘 봐
            return [AllowAny()]
        return [IsAuthenticated()]

    # 유효성 검사가 끝나고 나서
    # 실제  serializer.save()를 할 때 수행되는 함수
    def perform_create(self, serializer):
        # serializer.save는 commit=False를 지원하지 않음
        # 대신 키워드 인자를 통한 속성 지정을 지원함
        serializer.save(author=self.request.user)

