from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from adopt_review.serializers import ReviewSerializer
from adopt_review.models import Review


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
        serializer.save(user=self.request.user)

