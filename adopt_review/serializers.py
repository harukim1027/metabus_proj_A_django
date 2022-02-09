from django.contrib.auth import get_user_model
from rest_framework import serializers
from adopt_review.models import Review
from adopt_assignment.serializers import AssignmentSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["userID", "nickname"]


class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    adoptassignment = AssignmentSerializer(read_only=True)

    class Meta:
        model = Review
        fields = "__all__"

# ["review_no", "title", "content", "image1", "image2", "image3", "image4", "image5", "user", "adoptassignment"]