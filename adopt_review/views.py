from rest_framework import viewsets
from adopt_review.serializers import ReviewSerializer
from adopt_review.models import Review


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

