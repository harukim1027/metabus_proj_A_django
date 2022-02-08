from rest_framework import viewsets
from adopt_review.serializers import ReviewSerializer
from adopt_review.models import Review

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        query = self.request.query_params.get("query", "")
        if query:
            qs = qs.filter(animal__icontains=query)

        return qs
