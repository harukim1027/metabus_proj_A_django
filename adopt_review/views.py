from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from adopt_review.serializers import ReviewSerializer, ReviewCreateSerializer
from adopt_review.models import Review


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        if method == "GET":
            return ReviewSerializer
        return ReviewCreateSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        query = self.request.query_params.get("query", "")
        if query:
            qs = qs.filter(title__icontains=query) or qs.filter(review_no__icontains=query)

        return qs

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

