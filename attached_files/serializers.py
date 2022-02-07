from rest_framework import serializers
from accounts.models import User
from attached_files.models import Attached_file


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["nickname"]


class AttachedFileSerializer(serializers.ModelSerializer):
    nickname = AuthorSerializer(read_only=True)

    class Meta:
        model = Attached_file
        fields = ["notice_no", "att_file_no", "att_file"]

