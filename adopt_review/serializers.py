from rest_framework import serializers
from accounts.models import User
from adopt_review.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["review_no", "nickname", "title", "content", "image", "user"]

