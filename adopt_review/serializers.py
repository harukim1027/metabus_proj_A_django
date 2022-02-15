from django.contrib.auth import get_user_model
from rest_framework import serializers
from adopt_review.models import Review
from adopt_assignment.serializers import AssignmentSerializer


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
        depth = 2
# ["review_no", "title", "content", "image1", "image2", "image3", "image4", "image5", "user", "adoptassignment"]