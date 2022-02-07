from rest_framework import serializers
from accounts.models import User
from inquiry_board.models import Inquiry


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["nickname"]


class InquirySerializer(serializers.ModelSerializer):
    nickname = AuthorSerializer(read_only=True)

    class Meta:
        model = Inquiry
        fields = ["number", "nickname", "title", "content"]