from rest_framework import serializers
from adopt_review.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["review_no", "title", "content", "image", "user"]

