from typing import Dict
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.password_validation import validate_password
from django import forms
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer as OriginTokenObtainPairSerializer,
    TokenRefreshSerializer as OriginTokenRefreshSerializer,
)

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserCreationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    # nickname: CHAR(20) NOT NULL
    # name: CHAR(30) NOT NULL
    # password: CHAR(20) NOT NULL
    # phone_number: CHAR(16) NOT NULL
    # email: CHAR(50) NOT NULL
    # region: CHAR(20) NOT NULL
    # password_quiz: CHAR(30) NOT NULL
    # password_quiz_answer: CHAR(30) NOT NULL
    # created_at: DATETIME NOT NULL
    # updated_at: DATETIME NOT NULL

    class Meta:
        model = User
        fields = ["userID", "nickname", 'name', "password", "password2", "phone_number", "email", "region",
                  "password_quiz",
                  "password_quiz_answer"]

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError("동일한 비밀번호를 입력해주세요.")
        return attrs

    def create(self, validated_data):
        userID = validated_data["userID"]
        nickname = validated_data["nickname"]
        name = validated_data['name']
        phone_number = validated_data['phone_number']
        password = validated_data["password"]
        email = validated_data['email']
        region = validated_data["region"]
        password_quiz = validated_data['password_quiz']
        password_quiz_answer = validated_data['password_quiz_answer']

        new_user = User(userID=userID, nickname=nickname, name=name, phone_number=phone_number, email=email,
                        region=region, password_quiz=password_quiz,
                        password_quiz_answer=password_quiz_answer)
        new_user.set_password(password)
        new_user.save()

        return new_user


class TokenObtainPairSerializer(OriginTokenObtainPairSerializer):
    def validate(self, attrs):
        data: Dict = super().validate(attrs)
        data["userID"] = self.user.userID
        data["nickname"] = self.user.nickname
        data["name"] = self.user.name
        data["phone_number"] = self.user.phone_number
        data["email"] = self.user.email
        data["region"] = self.user.region
        data["password_quiz"] = self.user.password_quiz
        data["password_quiz_answer"] = self.user.password_quiz_answer
        data["is_staff"] = self.user.is_staff
        return data


class TokenRefreshSerializer(OriginTokenRefreshSerializer):
    pass


# password 전송을 위한 serializer (form의 메카니즘과 같다)
# class PasswordChangeSerializer(SetPasswordForm):
#     """
#     A form that lets a user change their password by entering their old
#     password.
#     """
#     error_messages = {
#         **SetPasswordForm.error_messages,
#         "password_incorrect": _(
#             "Your old password was entered incorrectly. Please enter it again."
#         ),
#     }
#     old_password = serializers.CharField(
#         label="Old password",
#         strip=False,
#         widget=serializers.CharField(
#             attrs={"autocomplete": "current-password", "autofocus": True}
#         ),
#     )
#
#     field_order = ["old_password", "new_password1", "new_password2"]
#
#     def clean_old_password(self):
#         """
#         Validate that the old_password field is correct.
#         """
#         old_password = self.cleaned_data["old_password"]
#         if not self.user.check_password(old_password):
#             raise ValidationError(
#                 self.error_messages["password_incorrect"],
#                 code="password_incorrect",
#             )
#         return old_password


class SetPasswordSerializer(forms.Form):
    """
    A form that lets a user change set their password without entering the old
    password -> 기존 패스워드를 입력할 필요 없이 변경할 수 있게 함
    """
    error_messages = {
        'password_mismatch': '동일한 패스워드를 입력해주세요 ! ',
    }
    new_password1 = forms.CharField(
        label="New password",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
    )
    new_password2 = forms.CharField(
        label="New password confirmation",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                raise ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
                )
        password_validation.validate_password(password2, self.user)
        return password2

    def save(self, commit=True):
        password = self.cleaned_data["new_password1"]
        self.user.set_password(password)
        if commit:
            self.user.save()
        return self.user
