from rest_framework import serializers
from adopt.models import Review
from django.contrib.auth import get_user_model


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["nickname"]


class ReviewSerializer(serializers.ModelSerializer):
    nickname = AuthorSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ["id", "nickname", "title", "content", "image"]

