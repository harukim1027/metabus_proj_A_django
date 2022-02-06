from typing import Dict

from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer as OriginTokenObtainPairSerializer,
    TokenRefreshSerializer as OriginTokenRefreshSerializer,
)

User = get_user_model()


class UserCreationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ["userID", "nickname", 'name', "password", "password2", "phone_number", "email", "region", "password_quiz",
                  "password_quiz_answer"]

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError("동일한 비밀번호를 입력해주세요.")
        return attrs

    def create(self, validated_data):
        userID = validated_data["userID"]
        nickname = validated_data["nickname"]
        name = validated_data['name']
        password = validated_data["password"]
        email = validated_data['email']
        region = validated_data["region"]
        password_quiz = validated_data['password_quiz']
        password_quiz_answer = validated_data['password_quiz_answer']

        new_user = User(usrerID=userID, nickname=nickname, name=name, email=email, region=region, password_quiz=password_quiz,
                        password_quiz_answer=password_quiz_answer)
        new_user.set_password(password)
        new_user.save()

        return new_user


class TokenObtainPairSerializer(OriginTokenObtainPairSerializer):
    def validate(self, attrs):
        data: Dict = super().validate(attrs)
        data["nickname"] = self.user.nickname
        return data


class TokenRefreshSerializer(OriginTokenRefreshSerializer):
    pass